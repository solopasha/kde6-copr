#!/usr/bin/bash
set -euxo pipefail

process_spec() {
    set -x
    baseName="$(sed -n 's/%global[[:space:]]\+\bframework\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$baseName" ]]; then
        baseName="$(rpmspec -q --srpm --qf "%{name}" "$1")"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    newCommit="$(grep "^${baseName};" frameworks-6.6.0-release-data | awk -F\; '{print $3}')"

    sed -i "s/$oldCommit/$newCommit/" "$1"
}
export -f process_spec

parallel process_spec :::: <(fd -espec)

