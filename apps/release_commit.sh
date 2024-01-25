#!/usr/bin/bash
set -euo pipefail

process_spec() {
    baseName="$(sed -n 's/%global[[:space:]]\+\bbase_name\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$baseName" ]]; then
        baseName="$(rpmspec -q --srpm --qf "%{name}" "$1")"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    newCommit="$(gh api -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" "repos/KDE/$baseName/tags" -q '.[] | select(.name=="v24.02.1") | .commit.sha')"

    sed -i "s/$oldCommit/$newCommit/" "$1"

}
export -f process_spec

parallel process_spec :::: <(fd -espec)
