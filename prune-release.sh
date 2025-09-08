#!/usr/bin/bash

now=$(date +%s)

gh release view "${BRANCH}" -R "${REPOSITORY}/${REPOSITORY_OWNER}" --json assets | jq -c '.assets[]' | while read -r asset; do
    name="$(echo "${asset}" | jq -r '.name')"
    updatedAt="$(echo "${asset}" | jq -r '.updatedAt' | date -f - +%s)"
    age=$((now - updatedAt))
    if [[ "${age}" -gt "18000" ]]; then
        gh release delete-asset "${BRANCH}" "${name}" -y -R "${REPOSITORY}/${REPOSITORY_OWNER}"
    fi

done
