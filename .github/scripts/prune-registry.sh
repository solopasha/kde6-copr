#!/usr/bin/bash
set -euo pipefail

: "${GH_TOKEN:?}"
: "${GITHUB_REPOSITORY:?}"
: "${GITHUB_REPOSITORY_OWNER:?}"
: "${REGISTRY_RETENTION_DAYS:?}"
: "${BATCH_RETENTION_DAYS:?}"
: "${DRY_RUN:?}"

[[ "${REGISTRY_RETENTION_DAYS}" =~ ^[0-9]+$ ]]
[[ "${BATCH_RETENTION_DAYS}" =~ ^[0-9]+$ ]]
(( REGISTRY_RETENTION_DAYS >= BATCH_RETENTION_DAYS ))
[[ "${DRY_RUN}" == true || "${DRY_RUN}" == false ]]

retry() {
  local attempt delay
  delay=1
  for attempt in 1 2 3 4 5; do
    if "$@"; then
      return 0
    fi
    if [[ "${attempt}" -lt 5 ]]; then
      printf 'Failed command:' >&2
      printf ' %q' "$@" >&2
      echo >&2
      echo "Attempt ${attempt}/5 failed; retrying in ${delay}s" >&2
      sleep "${delay}"
      delay=$((delay * 2))
    fi
  done
  return 1
}

retry_to_file() {
  local destination="$1"
  shift
  local attempt delay error_file temporary
  delay=1
  temporary="${destination}.tmp"
  error_file="${destination}.error"
  for attempt in 1 2 3 4 5; do
    if "$@" > "${temporary}" 2> "${error_file}"; then
      mv "${temporary}" "${destination}"
      rm -f "${error_file}"
      return 0
    fi
    if grep -Eqi 'not found|HTTP 404' "${error_file}"; then
      return 44
    fi
    cat "${error_file}" >&2
    if [[ "${attempt}" -lt 5 ]]; then
      printf 'Failed command:' >&2
      printf ' %q' "$@" >&2
      echo >&2
      echo "Attempt ${attempt}/5 failed; retrying in ${delay}s" >&2
      sleep "${delay}"
      delay=$((delay * 2))
    fi
  done
  return 1
}

owner_type="$(retry gh api "/repos/${GITHUB_REPOSITORY}" --jq '.owner.type')"
if [[ "${owner_type}" == Organization ]]; then
  package_scope="/orgs/${GITHUB_REPOSITORY_OWNER}"
elif [[ "${owner_type}" == User ]]; then
  package_scope="/users/${GITHUB_REPOSITORY_OWNER}"
else
  echo "Unsupported repository owner type: ${owner_type}" >&2
  exit 1
fi

{
  while IFS= read -r -d '' spec; do
    specfile="${spec##*/}"
    pkgname="${specfile%.spec}"
    printf '%s/%s\n' "${REPOSITORY}" "${pkgname,,}"
  done < <(find . -path './.git' -prune -o -type f -name '*.spec' -print0)
  printf '%s/%s\n' "${REPOSITORY}" buildroot
  printf '%s/%s\n' "${REPOSITORY}" repodata
  printf '%s/%s\n' "${REPOSITORY}" repository-batches
} | sort -u > /tmp/container-packages

now="$(date +%s)"
selected=0
deleted=0
while IFS= read -r package; do
  case "${package}" in
    "${REPOSITORY}"|"${REPOSITORY}/"*) ;;
    *) continue ;;
  esac
  encoded_package="$(jq -rn --arg value "${package}" '$value | @uri')"
  versions_endpoint="${package_scope}/packages/container/${encoded_package}/versions"
  if retry_to_file /tmp/package-versions gh api --paginate \
      "${versions_endpoint}?per_page=100"; then
    :
  elif [[ "$?" == 44 ]]; then
    continue
  else
    exit 1
  fi
  while IFS= read -r version; do
    id="$(jq -r '.id' <<< "${version}")"
    updated_at="$(jq -r '.updated_at' <<< "${version}")"
    mapfile -t tags < <(jq -r '.metadata.container.tags[]?' <<< "${version}")
    protected=false
    open_pr=false
    has_pr=false
    for tag in "${tags[@]}"; do
      if [[ "${tag}" == latest ]] || \
          [[ "${tag}" == latest-* && "${package}" != "${REPOSITORY}/repodata" ]]; then
        protected=true
      fi
      if [[ "${tag}" =~ ^pr-([0-9]+)- ]]; then
        has_pr=true
        pr_number="${BASH_REMATCH[1]}"
        pr_state="$(retry gh api "/repos/${GITHUB_REPOSITORY}/pulls/${pr_number}" --jq '.state')"
        if [[ "${pr_state}" == open ]]; then
          open_pr=true
        fi
      fi
    done
    if [[ "${protected}" == true || "${open_pr}" == true ]]; then
      continue
    fi

    retention_days="${REGISTRY_RETENTION_DAYS}"
    if [[ "${package}" == "${REPOSITORY}/repository-batches" ]]; then
      retention_days="${BATCH_RETENTION_DAYS}"
    fi
    updated_epoch="$(date -d "${updated_at}" +%s)"
    age_days=$(((now - updated_epoch) / 86400))
    if [[ "${has_pr}" != true && "${age_days}" -lt "${retention_days}" ]]; then
      continue
    fi

    tag_list="$(IFS=,; echo "${tags[*]}")"
    echo "Pruning ${package} version ${id} (${tag_list:-untagged}, ${age_days} days old)"
    selected=$((selected + 1))
    if [[ "${DRY_RUN}" == true ]]; then
      continue
    fi
    delete_endpoint="${versions_endpoint}/${id}"
    if ! retry gh api --method DELETE "${delete_endpoint}"; then
      if gh api "${delete_endpoint}" >/dev/null 2>&1; then
        exit 1
      fi
    fi
    deleted=$((deleted + 1))
  done < <(jq -c '.[]' /tmp/package-versions)
done < /tmp/container-packages

echo "Selected ${selected} GHCR versions; deleted ${deleted}"
