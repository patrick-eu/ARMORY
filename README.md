# Assemble — 让 AI Coding 更简单的开源武器库

> 按类别收录高星、持续维护的开源仓库，把它们喂给 AI（Claude Code / Cursor / Copilot…），让 vibe coding 更轻松地做出想要的效果。

**中文** | [English](README.en.md)

[![链接体检](https://github.com/patrick-eu/Assemble/actions/workflows/check.yml/badge.svg)](https://github.com/patrick-eu/Assemble/actions/workflows/check.yml)

## 怎么用

把这里收录的仓库"喂"给 AI 的常见姿势：

1. **直接给链接**：让 AI 参考某个仓库的用法写代码，例如"用 crawl4ai 帮我写一个抓取 XX 的脚本"。
2. **转成上下文**：用 [gitingest](https://github.com/coderamp-labs/gitingest) 把整个仓库变成一份纯文本，粘给 AI。
3. **接 MCP**：用 [context7](https://github.com/upstash/context7) 等 MCP 服务器，让 AI 实时查到最新文档，而不是靠过期记忆。
4. **抄模板**：直接 clone 收录的脚手架/模板仓库，让 AI 在成熟骨架上改，而不是从零瞎写。

## 收录标准

为了排除恶意代码和弃坑项目，收录的仓库必须同时满足：

- ⭐ **≥ 1000 stars**
- 🔄 **最近 6 个月内有提交**
- 📄 **开源协议明确**

标准由 [`check.py`](check.py) 自动校验，GitHub Actions 每周体检一次，不达标的会被移除。

---

## 🤖 AI 编程工具

直接帮你写代码的 Agent / 助手本体。

- [anthropics/claude-code](https://github.com/anthropics/claude-code) — 终端里的 AI 编程 Agent，理解整个代码库，执行多步任务。
- [cline/cline](https://github.com/cline/cline) — VS Code 里的自主编程 Agent，能创建/编辑文件、跑命令、用浏览器。
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — 开源 AI 软件工程师平台，能完成完整开发任务。
- [Aider-AI/aider](https://github.com/Aider-AI/aider) — 终端结对编程工具，直接在本地 git 仓库上改代码。
- [continuedev/continue](https://github.com/continuedev/continue) — 开源 IDE 助手，可自定义模型和上下文源。
- [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) — Cline 的社区增强分支，多模式 Agent 团队。

## 📝 提示词与规则

给 AI 定规矩、给灵感的资源库。

- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) — 各种技术栈的 .cursorrules 规则合集，拿来即用。
- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) — 经典提示词大全，写系统提示词的参考。
- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — 各大 AI 编程工具的系统提示词逆向合集，学习工具怎么"调教"模型。

## 📚 让 AI 读懂代码与文档

把仓库、网页、文档转成 AI 能吃的上下文。

- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) — 把任意 Git 仓库一键变成适合喂给 LLM 的纯文本摘要。
- [upstash/context7](https://github.com/upstash/context7) — MCP 服务器，让 AI 实时获取库的最新官方文档和示例代码。
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) — 给任意仓库自动生成 Wiki 文档，帮 AI 和人快速理解项目。

## 🕷️ 爬虫与数据采集

- [scrapy/scrapy](https://github.com/scrapy/scrapy) — Python 爬虫框架老大哥，生态成熟，AI 对它的用法非常熟。
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) — 为 LLM 设计的爬虫，输出干净的 Markdown，天生适合喂 AI。
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) — 把整站抓成 LLM-ready 的 Markdown/结构化数据，带 API。
- [apify/crawlee](https://github.com/apify/crawlee) — Node.js 爬虫与浏览器自动化库，反爬处理完善。
- [microsoft/playwright](https://github.com/microsoft/playwright) — 浏览器自动化标准件，动态页面抓取和 E2E 测试都靠它。

## 🎨 前端与 UI

让 AI 生成的界面不丑的关键。

- [shadcn-ui/ui](https://github.com/shadcn-ui/ui) — 复制即用的组件集，AI 生成 React 界面的事实标准。
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) — 原子化 CSS，AI 写样式的首选，训练语料最多。
- [saadeghi/daisyui](https://github.com/saadeghi/daisyui) — Tailwind 组件库，纯 class 就能出成品感界面。
- [ant-design/ant-design](https://github.com/ant-design/ant-design) — 企业级 React 组件库，中后台界面直接抄。

## 🏗️ 后端与全栈脚手架

在成熟骨架上让 AI 改，比从零生成靠谱得多。

- [fastapi/fastapi](https://github.com/fastapi/fastapi) — Python 高性能 API 框架，类型驱动，AI 生成的代码质量高。
- [nestjs/nest](https://github.com/nestjs/nest) — Node.js 企业级后端框架，结构清晰适合 AI 遵循。
- [supabase/supabase](https://github.com/supabase/supabase) — 开源 Firebase 替代品，数据库+认证+存储一条龙。
- [vercel/next.js](https://github.com/vercel/next.js) — React 全栈框架，AI 最熟悉的前端框架之一。

## 🔌 MCP 与 Agent 生态

给 AI 装外挂的基础设施。

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — MCP 官方服务器合集，文件系统、数据库、搜索等能力即插即用。
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 社区 MCP 服务器大全，找外挂先来这。
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — 构建有状态多 Agent 应用的框架。
- [microsoft/autogen](https://github.com/microsoft/autogen) — 微软的多 Agent 对话框架。

---

## 贡献

欢迎提 PR 收录新仓库，流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。核心要求：达到收录标准 + 一句话说清"对 AI coding 有什么用"。

## License

[CC0-1.0](LICENSE) — 内容随意使用。
