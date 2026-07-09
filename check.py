#!/usr/bin/env python3
"""体检 README.md 里收录的 GitHub 仓库：星数 >= 1000 且最近 6 个月内有提交。

用法: GITHUB_TOKEN=xxx python3 check.py [--update]
  --update  把 star 数和最后更新日期写回 README 条目（CI 每周自动执行）
  (token 可选，无 token 限流 60 次/小时)
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
SELF = "patrick-eu/ARMORY"
FILES = ("README.md", "README.en.md")
# 只匹配收录条目（以 "- [" 开头的 GitHub 链接），可选捕获已有的 `⭐…` 标注以便替换
LINK = re.compile(r"(- \[[^\]]+\]\(https://github\.com/([\w.-]+/[\w.-]+)[^)]*\))( `⭐[^`]*`)?")


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


def fmt_stars(n: int) -> str:
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def annotate(path: str, stats: dict) -> None:
    with open(path, encoding="utf-8") as f:
        src = f.read()

    def sub(m: re.Match) -> str:
        if info := stats.get(m.group(2)):
            return f"{m.group(1)} `⭐{fmt_stars(info[0])} · {info[1]}`"
        return m.group(1)

    out = LINK.sub(sub, src)
    if out != src:
        with open(path, "w", encoding="utf-8") as f:
            f.write(out)


def main() -> int:
    root = os.path.dirname(__file__) or "."
    text = "".join(
        open(os.path.join(root, name), encoding="utf-8").read() for name in FILES
    )
    repos = listed_repos(text)
    now = datetime.now(timezone.utc)
    failures = []
    stats = {}
    for repo in repos:
        try:
            data = fetch(repo)
        except urllib.error.HTTPError as e:
            failures.append(f"{repo}: HTTP {e.code}")
            continue
        stars = data["stargazers_count"]
        pushed = datetime.fromisoformat(data["pushed_at"].replace("Z", "+00:00"))
        idle = (now - pushed).days
        stats[repo] = (stars, pushed.date().isoformat())
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
    if "--update" in sys.argv:
        for name in FILES:
            annotate(os.path.join(root, name), stats)
        print("已把 star 数与更新日期写回 README")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
