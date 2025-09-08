#!/usr/bin/bash
set -euo pipefail

declare -A seen

WORKFLOW_FILE="$2"

get_needs() {
  local job=$1
  yq -r ".jobs.\"$job\".needs[]" "$WORKFLOW_FILE" 2>/dev/null
}

resolve_needs() {
  local job=$1

  if [[ -n "${seen[$job]:-}" ]]; then
    return
  fi
  seen[$job]=1

  local deps
  deps=$(get_needs "$job")

  for dep in $deps; do
    resolve_needs "$dep"
    echo "$dep"
  done
}

resolve_needs "$1" | sort -u
