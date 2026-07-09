# 贡献指南

## 收录一个新仓库

1. 确认它满足硬标准：
   - ⭐ ≥ 1000 stars
   - 🔄 最近 6 个月内有提交
   - 📄 有明确的开源协议
2. 在 README.md 对应类别下加一行，格式：
   ```markdown
   - [owner/repo](https://github.com/owner/repo) — 一句话说清对 AI coding 有什么用。
   ```
3. 本地跑 `python3 check.py` 确认全绿（可选，CI 也会跑）。
4. 提 PR，说明为什么值得收录。

## 新增类别

开 issue 讨论即可。原则：类别宁少勿多，每个类别至少能凑齐 3 个达标仓库再开。

## 移除仓库

CI 每周体检，不达标的仓库欢迎直接提 PR 移除。
