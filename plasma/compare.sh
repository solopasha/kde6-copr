#!/usr/bin/bash
set -euxo pipefail

process_spec() {
    set -x
    baseName="$(sed -n 's/%global[[:space:]]\+\bbase_name\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$baseName" ]]; then
        baseName="$(rpmspec -q --srpm --qf "%{name}" "$1")"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    newCommit="$(curl "https://invent.kde.org/api/v4/projects/plasma%2F${baseName}/repository/tags" | jq -r '.[] | select(.name=="v6.2.4") | .commit.id')"

    sed -i "s/$oldCommit/$newCommit/" "$1"
}
export -f process_spec

parallel process_spec :::: <(fd -espec)

