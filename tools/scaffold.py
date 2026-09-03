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
            cmds = sorted((repo / "cmd").glob("*/*.go")) if (repo / "cmd").is_dir() else []
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
