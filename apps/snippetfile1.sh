#!/usr/bin/bash
set -euxo pipefail

exclude_packages=(
    kf6.spec
)

IFS=" " read -r -a exclude_rendered <<< "$(printf -- "--exclude=%s " "${exclude_packages[@]}")"

process_spec() {
    set -x
    baseName="$(sed -n 's/%global[[:space:]]\+\bbase_name\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$baseName" ]]; then
        baseName="$(rpmspec -q --srpm --qf "%{name}" "$1")"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    newCommit="$(sed -n "/^${baseName}\s/{n;p}" snippetfile1.txt)"

    sed -i "s/$oldCommit/$newCommit/" "$1"
}
export -f process_spec

parallel process_spec :::: <(fd -espec "${exclude_rendered[@]}")

