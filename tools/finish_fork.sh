#!/bin/bash
# Push a verified fork and ensure main is its default branch (upstream forks
# often default to master, which would make the course README link show the
# wrong branch).
set -euo pipefail
cd "$1"
git push -f origin main
fork=$(basename -s .git "$(git remote get-url origin)")
[ "$(gh api "repos/ZhangZhuoSJTU/$fork" --jq .default_branch)" = main ] \
    || gh repo edit "ZhangZhuoSJTU/$fork" --default-branch main
echo "$fork: pushed, default branch main"
