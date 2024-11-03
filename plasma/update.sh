#!/usr/bin/bash
set -euo pipefail

# shellcheck source=/dev/null
. "$(which env_parallel.bash)"

process_spec() {
    baseName="$(sed -n 's/%global[[:space:]]\+\bbase_name\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$baseName" ]]; then
        baseName="$(rpmspec -q --srpm --qf "%{name}" "$1")"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    IFS=$'\n' read -r -d '' -a commits <<< "$(gh api --method GET "repos/KDE/$baseName/commits?sha=master&per_page=50" -q '.[].sha')"

    for commit in "${commits[@]}";
    do
        newCommit="$commit"
        if [[ $oldCommit == "$commit" ]]; then
            break
        fi
        message="$(gh api --method GET "repos/KDE/$baseName/commits/$commit" -q '.commit.message')"
        if [[ "$message" =~ ^(SVN|GIT)_SILENT[[:space:]](Sync[[:space:]]po/docbooks|made[[:space:]]messages) ]]; then
            continue
        fi
        break
    done

    sed -i "s/$oldCommit/$newCommit/" "$1"

    git diff --quiet -- "$1" || \
    { perl -pe 's/(?<=bumpver\s)(\d+)/$1 + 1/ge' -i "$1"; git diff --name-only -- "$1";}
}
export -f process_spec

parset changedSpecs process_spec :::: <(fd -espec)

git add -- '*.spec'
git commit -m "bump revisions"
git push --quiet origin plasma-6.3

# shellcheck disable=SC2154
# shellcheck disable=SC1083
xargs -a <(parallel echo {/.} ::: "${changedSpecs[@]}") ruby ~/ruby/deps.rb --copr solopasha/plasma-unstable -r f41 -s
