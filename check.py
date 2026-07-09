#!/usr/bin/env python3
"""体检 README.md 里收录的 GitHub 仓库：星数 >= 1000 且最近 6 个月内有提交。

用法: GITHUB_TOKEN=xxx python3 check.py  (token 可选，无 token 限流 60 次/小时)
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

MIN_STARS = 1000
MAX_IDLE_DAYS = 183
SELF = "patrick-eu/Assemble"


def listed_repos(readme: str) -> list[str]:
    repos = re.findall(r"https://github\.com/([\w.-]+/[\w.-]+)", readme)
    seen = []
    for r in repos:
        if r != SELF and r not in seen:
            seen.append(r)
    return seen


def fetch(repo: str) -> dict:
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    if token := os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main() -> int:
    root = os.path.dirname(__file__) or "."
    text = "".join(
        open(os.path.join(root, name), encoding="utf-8").read()
        for name in ("README.md", "README.en.md")
    )
    repos = listed_repos(text)
    now = datetime.now(timezone.utc)
    failures = []
    for repo in repos:
        try:
            data = fetch(repo)
        except urllib.error.HTTPError as e:
            failures.append(f"{repo}: HTTP {e.code}")
            continue
        stars = data["stargazers_count"]
        pushed = datetime.fromisoformat(data["pushed_at"].replace("Z", "+00:00"))
        idle = (now - pushed).days
        problems = []
        if stars < MIN_STARS:
            problems.append(f"仅 {stars} stars")
        if idle > MAX_IDLE_DAYS:
            problems.append(f"{idle} 天未更新")
        status = "; ".join(problems) if problems else "ok"
        print(f"{'✗' if problems else '✓'} {repo}: {stars} stars, {idle} 天前更新 ({status})")
        if problems:
            failures.append(f"{repo}: {status}")
    print(f"\n共 {len(repos)} 个仓库，{len(failures)} 个不达标")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
