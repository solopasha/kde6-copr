#!/usr/bin/bash

while getopts 'gfb' opt; do
    case "$opt" in
        g) export GITLAB=1 ;;
        f) export NO_FILTER=1 ;;
        b) export BETA=1 ;;
        *) echo "Usage $0 [-g] [-f] [-b]" >&2; exit 1
    esac
done
shift "$((OPTIND-1))"

if [[ "$BETA" == "1" ]]; then
    export REMOTE_BRANCH="Plasma/6.4"
else
    export REMOTE_BRANCH="master"
fi

exclude_packages=(
    kf6.spec
    kf6-kirigami.spec
)

IFS=" " read -r -a exclude_rendered <<< "$(printf -- "--exclude=%s " "${exclude_packages[@]}")"

process_spec() {
    baseName="$(sed -n 's/%global[[:space:]]\+\b\(framework\|base_name\)\b[[:space:]]\+\(.*\)/\2/p' "$1")"
    if [[ -z "$baseName" ]]; then
        specfile="$(basename "$1")"
        baseName="${specfile%.*}"
    fi

    oldCommit="$(sed -n 's/%global[[:space:]]\+\bcommit0\b[[:space:]]\+\(.*\)/\1/p' "$1")"
    if [[ -z "$oldCommit" ]]; then
        exit 1
    fi

    if [[ "$GITLAB" == "1" ]]; then
        nameWithNamepsace="$(echo 'local kde_maps = require "frameworks/kf6/kde_maps"; print((kde_maps[arg[1]]:gsub("/", "%%2F")))' | luajit - "$baseName")"
        mapfile -t commits < <(curl --retry 5 -Ss "https://invent.kde.org/api/v4/projects/${nameWithNamepsace}/repository/commits?ref_name=${REMOTE_BRANCH}&per_page=50" | jq -c '.[]')
    else
        mapfile -t commits < <(gh api --method GET "repos/KDE/$baseName/commits?sha=${REMOTE_BRANCH}&per_page=50" | jq -c '.[]')
    fi

    for commit in "${commits[@]}";
    do
        newCommit="$(jq -r '.id, .sha | values' <<< "$commit")"
        if [[ $oldCommit == "$newCommit" ]]; then
            break
        fi
        if [[ $NO_FILTER != "1" ]]; then
            message="$(jq -r '.commit.message, .message | values' <<< "$commit")"
            if [[ "$message" =~ (SVN|GIT)_SILENT|Update[[:space:]]version[[:space:]]to|Update[[:space:]]dependency[[:space:]]version[[:space:]]to|[Uu]pdate[[:space:]]version[[:space:]]for[[:space:]]new[[:space:]]release|snapcraft:|as[[:space:]]hardened[[:space:]]was[[:space:]]reverted[[:space:]]from[[:space:]]ECM|Haiku|Update[[:space:]]version[[:space:]]number[[:space:]]for[[:space:]]5\.27\.12|appiumtests:|Lower[[:space:]]Python[[:space:]]requirement[[:space:]]to[[:space:]]3\.9|^CI:|Enable[[:space:]]Python[[:space:]]bindings[[:space:]]on[[:space:]]FreeBSD|autotests:|^doc:|metainfo.yaml$|Add[[:space:]]xml/yaml[[:space:]]linting|^Appdata:|Fix[[:space:]]build[[:space:]]with[[:space:]]Qt[[:space:]]6\.10|It[[:space:]]compiles[[:space:]]fine[[:space:]]without[[:space:]]qt6\.9[[:space:]]deprecated[[:space:]]methods|It[[:space:]]compiles[[:space:]]fine[[:space:]]without[[:space:]]kf6\.1[[:digit:]][[:space:]]deprecated[[:space:]]methods|include[[:space:]]quiet[[:space:]]packages[[:space:]]in[[:space:]]the[[:space:]]feature[[:space:]]summary|It[[:space:]]compiles[[:space:]]fine[[:space:]]without[[:space:]]kf_6_1[[:digit:]][[:space:]]deprecated[[:space:]]methods|Remove[[:space:]]unused[[:space:]]PROJECT_VERSION_MAJOR[[:space:]]variable|Remove[[:space:]](code|conditions)[[:space:]]for[[:space:]]no[[:space:]]longer[[:space:]]supported[[:space:]]Qt[[:space:]]versions|^flatpak:|Port[[:space:]]API[[:space:]]documentation[[:space:]]to[[:space:]]QDoc[[:space:]]syntax|It[[:space:]]compiles[[:space:]]fine[[:space:]]without[[:space:]]deprecated[[:space:]]methods|Add[[:space:]]landing[[:space:]]page[[:space:]]for[[:space:]]QDoc|Documentation[[:space:]]fixes|Add[[:space:]]missing[[:space:]]QDoc[[:space:]]dependencies|Add[[:space:]]missing[[:space:]]qhp[[:space:]]projects|Remove[[:space:]]leftover[[:space:]]doxygen[[:space:]]file|Add[[:space:]]missing[[:space:]]qhp[[:space:]]project|Add[[:space:]]tags[[:space:]]file[[:space:]]to[[:space:]]documentation|It[[:space:]]compiles[[:space:]]fine[[:space:]]without[[:space:]]qt[[:space:]]6.[[:digit:]][[:digit:]][[:space:]]deprecated[[:space:]]methods|It[[:space:]]compiles[[:space:]]fine[[:space:]]without[[:space:]]kf[[:space:]]6.[[:digit:]][[:digit:]][[:space:]]deprecated[[:space:]]methods|Bump[[:space:]]kf[[:space:]]ecm_set_disabled_deprecation_versions|Add[[:space:]]QML[[:space:]]linting|Add[[:space:]]linting|Reformat[[:space:]]\.kde-ci\.yml|Enable[[:space:]]qmllint[[:space:]]in[[:space:]]CI|Add[[:space:]]missing[[:space:]]CI[[:space:]]dep|Update[[:space:]]plasma-wayland-protocols[[:space:]]dep[[:space:]]version ]]; then
                continue
            fi
        fi
        break
    done
    if [[ -z "$newCommit" ]]; then
        echo "$1"
        exit 1
    fi

    sed -i "s/$oldCommit/$newCommit/" "$1"

    git diff --quiet -- "$1" || \
    { perl -pe 's/(?<=bumpver\s)(\d+)/$1 + 1/ge;' -pe 's/(^Release:\s+)(\d+)(%.*)/${1}1${3}/' -i "$1"; }
}
export -f process_spec

parallel process_spec :::: <(fd -espec . './plasma' './frameworks' './related/plasma-wayland-protocols' "${exclude_rendered[@]}")
