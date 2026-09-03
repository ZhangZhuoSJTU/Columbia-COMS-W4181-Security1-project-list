# ProgramBench Project Porting Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Port all 198 ProgramBench projects into per-project course harness repos (fork → pin commit → `compile.sh` + `test.sh` → gold-verify → push), in 10-project batches.

**Architecture:** A scaffold script generates each project repo from the ProgramBench task data and a shared `test.sh` template; a porter then adapts `compile.sh` if needed, verifies the unmodified ("gold") source passes 100% of scored tests locally, pushes the fork, and records the kept-test count in the course README table.

**Tech Stack:** bash, python3 (≥3.11, for `tomllib`), `gh` CLI, git, Go/Rust/C toolchains, pytest (installed per-repo by `test.sh`).

**Spec:** The reference implementation is `github.com/ZhangZhuoSJTU/yj` (commit "Add ProgramBench compile and test harness") — every ported repo must match its shape. Process constraints came from the course owner and are listed below.

## Global Constraints

- **compile.sh principle:** compiles the *current working tree* (students' local edits included) into `./executable` at the repo root. Nothing else.
- **test.sh principle:** runs `./compile.sh` first, then downloads (cached) and runs every active ProgramBench test branch against the fresh binary, excluding ignored tests, and prints per-branch + total summary with ignored counts.
- **No Docker.** Everything runs natively on macOS and Linux; requirements per repo are only the language toolchain + `python3` + `curl`.
- **Gold verification gate:** on the unmodified pinned source, `./test.sh` must report `TOTAL: N/N passed (100.0%)`. Any shortfall is investigated (portability, not test bugs) before push; unresolvable platform issues are recorded in `.programbench/NOTES.md` and flagged in the batch report.
- Fixed portability measures already in the template (do not remove): `TZ=UTC`, `sed` rewrite of `cd /workspace` → relocatable, `--timeout-method=thread` → `signal`.
- Commits: one-sentence messages, **no Claude co-author trailers**. Harness commit message is always `Add ProgramBench compile and test harness`. Force-push `main` (fork's main is being redefined to the pinned commit).
- GitHub account: `ZhangZhuoSJTU`. Fork-name collisions: `astaxie/bat` → `bat-astaxie`, `sharkdp/bat` → `bat-sharkdp`.
- Paths: project clones live in `~/Code/course-competition/<fork-name>/`; tooling and this plan live in the `Columbia-COMS-W4181-Security1-project-list` repo; ProgramBench task data is read from `~/Code/ProgramBench/src/programbench/data/tasks/`.

---

### Task 1: `tools/test.sh.template` + `tools/scaffold.py`

**Files:**
- Create: `tools/test.sh.template`
- Create: `tools/scaffold.py`
- Test: regenerate yj's harness in place and confirm a clean `git status`

**Interfaces:**
- Produces: `tools/scaffold.py <instance_id> [--no-fork]` — forks (unless `--no-fork`), clones to `~/Code/course-competition/<fork>`, pins `main`, writes `compile.sh`, `test.sh`, `.programbench/branches.txt`, `.programbench/ignored_tests.txt`, appends `.gitignore` block. With `--no-fork` it only (re)generates files into an existing clone.

- [ ] **Step 1: Create `tools/test.sh.template`** — the yj `test.sh` with the instance id replaced by `@@INSTANCE@@`:

```bash
#!/bin/bash
# Compile, then run all ProgramBench test branches for @@INSTANCE@@.
#
# Test suites (one tarball per "branch") are downloaded from the public
# ProgramBench-Tests HuggingFace dataset on first run and cached under
# .programbench/tests/. Each branch is extracted into .programbench/run/<branch>,
# the freshly built ./executable is copied in (replacing the linux binary the
# tarball ships), and the branch's own eval/run.sh drives pytest, writing JUnit
# XML to eval/results.xml. Tests listed in .programbench/ignored_tests.txt are
# excluded from the final score, mirroring `programbench info`.
set -euo pipefail
cd "$(dirname "$0")"

# The reference results were produced in UTC containers; datetime-handling
# tests are timezone-sensitive, so pin TZ for reproducibility everywhere.
export TZ=UTC

INSTANCE=@@INSTANCE@@
BASE_URL="https://huggingface.co/datasets/programbench/ProgramBench-Tests/resolve/main/$INSTANCE/tests"
PB=.programbench

./compile.sh

if [ ! -d "$PB/venv" ]; then
    python3 -m venv "$PB/venv"
    "$PB/venv/bin/pip" install -q pytest pytest-timeout pytest-xdist
fi
export PATH="$PWD/$PB/venv/bin:$PATH"

mkdir -p "$PB/tests"
while read -r branch; do
    tar="$PB/tests/$branch.tar.gz"
    [ -f "$tar" ] || curl -fsSL -o "$tar" "$BASE_URL/$branch.tar.gz"
    dir="$PB/run/$branch"
    rm -rf "$dir" && mkdir -p "$dir"
    tar xzf "$tar" -C "$dir"
    cp executable "$dir/executable" && chmod +x "$dir/executable"
    # Some branches hardcode the container's /workspace path; make run.sh
    # relocatable. Also use signal-based timeouts (as programbench eval does)
    # so a timing-out test fails cleanly instead of killing the pytest worker.
    sed -i.bak -e 's|cd /workspace|cd "$(dirname "$0")/.."|' \
        -e 's/--timeout-method=thread/--timeout-method=signal/g' \
        "$dir/eval/run.sh" && rm -f "$dir/eval/run.sh.bak"
    echo "=== branch $branch ==="
    (cd "$dir" && bash eval/run.sh > run.log 2>&1 || true)
done < "$PB/branches.txt"

python3 - <<'EOF'
import xml.etree.ElementTree as ET
from pathlib import Path

ignored = set(Path(".programbench/ignored_tests.txt").read_text().split())
total = passed = dropped = 0
for branch in Path(".programbench/branches.txt").read_text().split():
    xml = Path(f".programbench/run/{branch}/eval/results.xml")
    if not xml.exists():
        print(f"{branch}: NO RESULTS (see .programbench/run/{branch}/run.log)")
        continue
    n = ok = skip = 0
    for case in ET.fromstring(xml.read_text()).iter("testcase"):
        name = f"{case.get('classname')}.{case.get('name')}"
        if f"{branch}/{name}" in ignored:
            skip += 1
            continue
        n += 1
        ok += not [c for c in case if c.tag in ("failure", "error", "skipped")]
    print(f"{branch}: {ok}/{n} passed ({skip} ignored)")
    total += n
    passed += ok
    dropped += skip
print(f"\nTOTAL: {passed}/{total} passed ({100 * passed / total:.1f}%), {dropped} tests ignored")
EOF
```

- [ ] **Step 2: Verify the template matches the yj reference** (guards against template drift):

Run: `sed 's/@@INSTANCE@@/sclevine__yj.8016400/' tools/test.sh.template | diff - ~/Code/course-competition/yj/test.sh`
Expected: no output (identical).

- [ ] **Step 3: Create `tools/scaffold.py`:**

```python
#!/usr/bin/env python3
"""Scaffold a harness repo for one ProgramBench instance.

Forks the upstream repo (unless --no-fork), clones it next to this repo's
clone, pins main to the benchmark commit, and generates compile.sh, test.sh
and .programbench/ metadata. Verification and pushing are manual follow-ups.

Usage: tools/scaffold.py <instance_id> [--no-fork]
"""

import json
import re
import subprocess
import sys
import time
import tomllib
from pathlib import Path

GH_USER = "ZhangZhuoSJTU"
TASKS_DIR = Path.home() / "Code/ProgramBench/src/programbench/data/tasks"
TOOLS = Path(__file__).resolve().parent
DEST_ROOT = TOOLS.parent.parent
FORK_RENAMES = {"astaxie/bat": "bat-astaxie", "sharkdp/bat": "bat-sharkdp"}

GITIGNORE_BLOCK = """
# ProgramBench course-competition artifacts
executable
.programbench/venv/
.programbench/tests/
.programbench/run/
"""


def sh(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


def compile_body(repo: Path, language: str) -> str:
    if language == "go":
        target = "."
        if not any(re.search(r"^package main\b", p.read_text(), re.M) for p in repo.glob("*.go")):
            cmds = sorted((repo / "cmd").glob("*/main.go")) if (repo / "cmd").is_dir() else []
            if cmds:
                target = f"./cmd/{cmds[0].parent.name}"
        return f"go build -o executable {target}"
    if language == "rs":
        cargo = tomllib.loads((repo / "Cargo.toml").read_text())
        name = cargo["package"]["name"]
        for b in cargo.get("bin", []):
            name = b.get("name", name)
        return f'cargo build --release\ncp "target/release/{name}" executable'
    return "make\n# TODO(porter): copy the built binary: cp <path-to-binary> executable\nexit 1"


def main() -> None:
    iid = sys.argv[1]
    no_fork = "--no-fork" in sys.argv
    task = dict(
        line.split(": ", 1) for line in (TASKS_DIR / iid / "task.yaml").read_text().splitlines() if ": " in line
    )
    repository, commit, language = task["repository"], task["commit"], task["language"]
    fork = FORK_RENAMES.get(repository, repository.split("/")[1])
    repo = DEST_ROOT / fork

    if not no_fork:
        cmd = ["gh", "repo", "fork", repository, "--clone=false"]
        if repository in FORK_RENAMES:
            cmd += ["--fork-name", fork]
        subprocess.run(cmd, check=True)
        for _ in range(5):
            if subprocess.run(["git", "clone", f"git@github.com:{GH_USER}/{fork}.git", str(repo)]).returncode == 0:
                break
            time.sleep(5)
        else:
            sys.exit(f"could not clone fork {fork}")
        if subprocess.run(["git", "cat-file", "-e", commit], cwd=repo).returncode != 0:
            sh("git", "fetch", f"https://github.com/{repository}", commit, cwd=repo)
        sh("git", "checkout", "-q", "-B", "main", commit, cwd=repo)

    branches = json.loads((TASKS_DIR / iid / "tests.json").read_text())["branches"]
    active = {b: info for b, info in sorted(branches.items()) if not info.get("ignored")}
    (repo / ".programbench").mkdir(exist_ok=True)
    (repo / ".programbench/branches.txt").write_text("\n".join(active) + "\n")
    (repo / ".programbench/ignored_tests.txt").write_text(
        "".join(f"{b}/{t['name']}\n" for b, info in active.items() for t in info.get("ignored_tests") or [])
    )
    (repo / "test.sh").write_text((TOOLS / "test.sh.template").read_text().replace("@@INSTANCE@@", iid))
    (repo / "compile.sh").write_text(
        "#!/bin/bash\n"
        "# ProgramBench-style build: must produce ./executable at the repo root.\n"
        "set -e\n"
        'cd "$(dirname "$0")"\n'
        f"{compile_body(repo, language)}\n"
    )
    for script in ("compile.sh", "test.sh"):
        (repo / script).chmod(0o755)
    gitignore = repo / ".gitignore"
    existing = gitignore.read_text() if gitignore.exists() else ""
    if ".programbench/venv/" not in existing:
        gitignore.write_text(existing.rstrip("\n") + ("\n" if existing else "") + GITIGNORE_BLOCK)
    print(f"scaffolded {repo} at {commit[:7]} — review compile.sh, then run ./test.sh")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Test scaffold against the yj reference.** Regenerating yj's harness in its existing clone must be a no-op against what is committed:

Run: `chmod +x tools/scaffold.py && tools/scaffold.py sclevine__yj.8016400 --no-fork && git -C ~/Code/course-competition/yj status --porcelain`
Expected: scaffold prints the "scaffolded ..." line; `git status --porcelain` prints **nothing** (all generated files byte-identical to the committed reference).

- [ ] **Step 5: Commit**

```bash
git add tools/test.sh.template tools/scaffold.py
git commit -m "Add scaffold tooling for porting ProgramBench projects"
```

### Task 2: `tools/update_readme.py`

**Files:**
- Create: `tools/update_readme.py`
- Test: idempotence on the yj row, failure on unknown rows

**Interfaces:**
- Produces: `tools/update_readme.py <owner/repo> <tests_kept>` — rewrites exactly one "Tests kept" cell in `README.md`, exits non-zero unless exactly one row matched.

- [ ] **Step 1: Create `tools/update_readme.py`:**

```python
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
```

- [ ] **Step 2: Positive test (yj row already says 768 → must be a no-op):**

Run: `chmod +x tools/update_readme.py && tools/update_readme.py sclevine/yj 768 && git diff --exit-code README.md`
Expected: prints `updated sclevine/yj: tests kept = 768`; `git diff` exits 0 (no change).

- [ ] **Step 3: Negative test:**

Run: `tools/update_readme.py nosuch/repo 5; echo "exit=$?"`
Expected: `expected exactly 1 row for nosuch/repo, matched 0` and `exit=1`.

- [ ] **Step 4: Commit**

```bash
git add tools/update_readme.py
git commit -m "Add README table updater"
git push
```

### Task 3: Port batch 1 (10 projects)

Batch 1 = easy, non-TUI, non-network CLI tools with light build dependencies (6 Rust, 4 Go):

| # | instance_id | lang | expected compile core |
|---|---|---|---|
| 1 | `anordal__shellharden.6a6ffd4` | rs | `cargo build --release && cp target/release/shellharden executable` |
| 2 | `mgdm__htmlq.6e31bc8` | rs | `cp target/release/htmlq executable` |
| 3 | `wfxr__csview.8ac4de0` | rs | `cp target/release/csview executable` |
| 4 | `rbakbashev__elfcat.52f8cc7` | rs | `cp target/release/elfcat executable` |
| 5 | `sirwart__ripsecrets.34c9e03` | rs | `cp target/release/ripsecrets executable` |
| 6 | `clog-tool__clog-cli.7066cba` | rs | binary name from Cargo.toml (likely `clog`) |
| 7 | `kisielk__errcheck.dacab89` | go | `go build -o executable .` |
| 8 | `mibk__dupl.1bf052b` | go | `go build -o executable .` |
| 9 | `psampaz__go-mod-outdated.bb79367` | go | `go build -o executable .` |
| 10 | `eliukblau__pixterm.1a93fd5` | go | `go build -o executable ./cmd/pixterm` (scaffold auto-detects) |

**For EACH project, in order, run this identical procedure** (shown once; substitute the instance id and fork dir):

- [ ] **Step A: Scaffold**

Run: `tools/scaffold.py <instance_id>`
Expected: fork created on GitHub, clone at `~/Code/course-competition/<fork>`, `main` pinned, harness files written. Inspect the generated `compile.sh` — it must match the "expected compile core" above; fix it if scaffold guessed wrong.

- [ ] **Step B: Compile check**

Run: `cd ~/Code/course-competition/<fork> && ./compile.sh && test -x executable && echo OK`
Expected: `OK`. Contingencies with exact fixes:
- Go project without `go.mod` (pre-modules era): prepend to `compile.sh`: `[ -f go.mod ] || { go mod init github.com/<owner>/<repo>; go mod tidy; }`
- Rust lockfile version conflicts: `cargo build --release` already ignores `--locked`; if a dependency fails to build on the modern toolchain, record the exact error in `.programbench/NOTES.md` and escalate to the batch report rather than patching source.

- [ ] **Step C: Gold verification**

Run: `./test.sh 2>&1 | tail -15`
Expected: every branch reports `N/N passed`, final line `TOTAL: X/X passed (100.0%), K tests ignored`. If any branch shows `NO RESULTS`, read `.programbench/run/<branch>/run.log` — the known causes and fixes are already in the template (workspace path, timeout method); a new cause means debugging with the superpowers:systematic-debugging skill before any push. If individual tests fail, diagnose for environment sensitivity (TZ-like issues); harness-level fixes go in `test.sh`/template, never in test files. Record any residual platform-specific failures in `.programbench/NOTES.md` and note them in the batch report; such a project is pushed but its README row gets a `*` footnote instead of a clean count.

- [ ] **Step D: Commit and push the fork**

```bash
git add -A
git commit -m "Add ProgramBench compile and test harness"
git push -f origin main
```

- [ ] **Step E: Record in course README** (from the Columbia repo clone)

Run: `tools/update_readme.py <owner/repo> <X-from-TOTAL-line>`
Expected: `updated <owner/repo>: tests kept = <X>`.

- [ ] **Batch close-out: commit the README once, push, and report**

```bash
git add README.md
git commit -m "Record batch 1 ported projects"
git push
```

Report to the course owner: per-project TOTAL lines, any `NOTES.md` deviations, template changes made (if the template changed, re-run `tools/scaffold.py sclevine__yj.8016400 --no-fork` and push the regenerated yj `test.sh` so all repos stay in sync).

### Task 4: Batches 2–20 (repeatable procedure)

Each subsequent batch reuses Task 3's Steps A–E verbatim per project plus the same close-out. What changes is only project selection. Selection order for remaining 188:

1. Remaining **easy+medium Rust/Go CLI** tools (non-TUI, non-network).
2. **Simple C** projects (`cmatsuoka__figlet`, `lh3__seqtk`, `madler__pigz`, `lz4__lz4`, `facebook__zstd`, ... — `compile.sh` is hand-written per project: `make` + `cp <binary> executable`).
3. **Harder Rust/Go** (bigger builds: `burntsushi__ripgrep`, `sharkdp__bat`, `ast-grep__ast-grep`, ...).
4. **TUI / network / platform-sensitive** tools (`htop`, `tty-clock`, `gping`, `pingu`, `entr`, ...) — expect gold-verification failures locally; budget debugging time and expect more `NOTES.md` entries.
5. **Heavyweight C/C++ builds last** (`ffmpeg`, `duckdb`, `sqlite`, `php-src`, `gdal`, `gromacs`, `doxygen`, ...) — long compiles, autotools/cmake dependencies; each needs a bespoke `compile.sh` and may need `brew`/`apt` prerequisites documented in `.programbench/NOTES.md`.

At the start of each batch: pick the next 10 unported rows (README rows still `N/A`) per this ordering, list them in the batch report, then execute. A batch is done only when all 10 forks are pushed and the README commit lands.

## Self-Review Notes

- Spec coverage: harness shape (Tasks 1, 3), README recording (Tasks 2, 3E), all 198 projects (Task 4 ordering covers the remainder), batch size 10 (Tasks 3–4). ✓
- The gold-verification gate is the only "test suite" that matters per project; tooling tasks carry their own executable checks against the yj reference. ✓
- Type/name consistency: `tools/scaffold.py`, `tools/update_readme.py`, `tools/test.sh.template`, `.programbench/{branches.txt,ignored_tests.txt,NOTES.md}` used identically throughout. ✓
