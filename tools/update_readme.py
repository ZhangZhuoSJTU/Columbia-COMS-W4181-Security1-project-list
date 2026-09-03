#!/usr/bin/env python3
"""Set the 'Tests kept' cell for one project row in README.md.

Usage: tools/update_readme.py <owner/repo> <tests_kept>
"""

import re
import sys
from pathlib import Path

readme = Path(__file__).resolve().parent.parent / "README.md"
repo, kept = sys.argv[1], sys.argv[2]
pattern = re.compile(
    rf"^(\| \[{re.escape(repo)}\]\([^)]+\) \| `[0-9a-f]{{7}}` \| \d+ \| )\S+( \|.*)$", re.M
)
new, n = pattern.subn(rf"\g<1>{kept}\g<2>", readme.read_text())
if n != 1:
    sys.exit(f"expected exactly 1 row for {repo}, matched {n}")
readme.write_text(new)
print(f"updated {repo}: tests kept = {kept}")
