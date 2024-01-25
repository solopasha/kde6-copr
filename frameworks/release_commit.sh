#!/usr/bin/bash
set -euo pipefail

# shellcheck source=/dev/null
. "$(which env_parallel.bash)"

exclude_packages=(
    kf6.spec
)

IFS=" " read -r -a exclude_rendered <<< "$(printf -- "--exclude=%s " "${exclude_packages[@]}")"

process_spec() {
    set -x
    baseName="$(sed -n 's/%global[[:space:]]\+\bframework\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$baseName" ]]; then
        baseName="$(rpmspec -q --srpm --qf "%{name}" "$1")"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    newCommit="$(curl -sS "https://invent.kde.org/api/v4/projects/frameworks%2F$baseName/repository/tags" | jq -r '.[] | select(.name=="v6.0.0") | .commit.id')"

    sed -i "s/$oldCommit/$newCommit/" "$1"

    git diff --quiet -- "$1" || \
    { perl -pe 's/(?<=bumpver\s)(\d+)/$1 + 1/ge' -i "$1"; }
}
export -f process_spec

parallel process_spec :::: <(fd -espec "${exclude_rendered[@]}")

