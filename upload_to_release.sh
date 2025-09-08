#!/usr/bin/bash

set -eo pipefail

TAG="${TAG:-unstable}"
MAX_RETRIES=5

upload_file() {
  local file="$1"
  local attempt=1

  if [[ -f assets.list && "$(basename "$file")" != "packages.txt" ]]; then
    if grep -q "$(basename "$file")" assets.list; then
      # echo "$(basename "$file") already exists"
      exit 0
    fi
  fi

  while (( attempt <= MAX_RETRIES )); do
    local response
    response=$(gh api rate_limit)
    local remaining
    remaining=$(echo "$response" | jq '.rate.remaining')
    local reset
    reset=$(echo "$response" | jq '.rate.reset')
    local now
    now=$(date +%s)

    if [[ "$remaining" -le 1 ]]; then
        local wait_time=$((reset - now + 5))
        echo "🔒 GitHub API limit hit. Sleeping for $wait_time seconds..."
        sleep "$wait_time"
    fi

    if gh release upload "$TAG" "$file" --repo "${REPOSITORY_OWNER}/${REPOSITORY}" --clobber; then
      echo "✅ Uploaded: $file to $TAG"
      exit 0
    else
      echo "Upload failed for $file. Retrying in $((2 ** attempt))s..."
      sleep $((2 ** attempt))
      ((attempt++))
    fi
  done

  echo "❌ Failed to upload $file after $MAX_RETRIES attempts."
  exit 1
}

export -f upload_file
export TAG REPOSITORY REPOSITORY_OWNER MAX_RETRIES

gh release view "${TAG}" --repo "${REPOSITORY_OWNER}/${REPOSITORY}" --json assets | jq -r '.assets[].name' > assets.list || :

parallel --halt now,fail=1 --jobs 5 upload_file ::: "$@"
