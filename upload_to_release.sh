#!/usr/bin/bash

set -eo pipefail

TAG="${TAG:-unstable}"
MAX_RETRIES=5

upload_file() {
  local file="$1"
  local attempt=1

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
      echo "✅ Uploaded: $file"
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

parallel --jobs 5 --delay 0.1 upload_file ::: "$@"
