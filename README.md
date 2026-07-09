# ARMORY — 让 AI Coding 更简单的开源武器库

> 按类别收录高星、持续维护的开源仓库，把它们喂给 AI（Claude Code / Cursor / Copilot…），让 vibe coding 更轻松地做出想要的效果。

**中文** | [English](README.en.md)

[![链接体检](https://github.com/patrick-eu/ARMORY/actions/workflows/check.yml/badge.svg)](https://github.com/patrick-eu/ARMORY/actions/workflows/check.yml)

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
- [openai/codex](https://github.com/openai/codex) — OpenAI 的终端编程 Agent，Rust 实现，轻量快速。
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) — Google 开源的终端 AI Agent，直连 Gemini。
- [anomalyco/opencode](https://github.com/anomalyco/opencode) — 开源终端 AI 编程 Agent，模型随便换。
- [aaif-goose/goose](https://github.com/aaif-goose/goose) — 本地运行的开源 AI Agent，可装扩展自动化工程任务。
- [TabbyML/tabby](https://github.com/TabbyML/tabby) — 自托管 AI 代码补全，Copilot 的开源替代。
- [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) — VS Code 开源 AI Agent，集 Cline/Roo 之长。

## 📝 提示词与规则

给 AI 定规矩、给灵感的资源库。

- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) — 各种技术栈的 .cursorrules 规则合集，拿来即用。
- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) — 经典提示词大全，写系统提示词的参考。
- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — 各大 AI 编程工具的系统提示词逆向合集，学习工具怎么"调教"模型。
- [anthropics/skills](https://github.com/anthropics/skills) — Anthropic 官方 Agent Skills 合集，给 Claude 装领域技能。
- [obra/superpowers](https://github.com/obra/superpowers) — 编程 Agent 技能全家桶：头脑风暴、TDD、系统化调试等工作流。
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) — 提示词工程系统教程，论文、技巧、案例俱全。
- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) — Anthropic 官方交互式提示词教程。
- [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) — 提示词技术实战教程集，从基础到高级都带代码。
- [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) — 精选高分 GPTs 提示词与提示词工程资料。

## 📚 让 AI 读懂代码与文档

把仓库、网页、文档转成 AI 能吃的上下文。

- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) — 把任意 Git 仓库一键变成适合喂给 LLM 的纯文本摘要。
- [upstash/context7](https://github.com/upstash/context7) — MCP 服务器，让 AI 实时获取库的最新官方文档和示例代码。
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) — 给任意仓库自动生成 Wiki 文档，帮 AI 和人快速理解项目。
- [yamadashy/repomix](https://github.com/yamadashy/repomix) — 把整个代码库打包成一份 AI 友好的文件，gitingest 的热门同类。
- [microsoft/markitdown](https://github.com/microsoft/markitdown) — 微软出品，Office/PDF 等各种文件转 Markdown 喂 LLM。
- [docling-project/docling](https://github.com/docling-project/docling) — IBM 开源文档解析器，PDF/表格/版面理解，输出结构化数据。
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) — 高质量 PDF 转 Markdown/JSON，公式表格都能抽。
- [datalab-to/marker](https://github.com/datalab-to/marker) — PDF 快速精准转 Markdown，公式表格支持好。
- [jina-ai/reader](https://github.com/jina-ai/reader) — 任意 URL 前加 r.jina.ai 即得 LLM 友好的正文文本。
- [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) — 各种格式文档的 ETL 预处理库，RAG 数据管道常客。

## 🕷️ 爬虫与数据采集

- [scrapy/scrapy](https://github.com/scrapy/scrapy) — Python 爬虫框架老大哥，生态成熟，AI 对它的用法非常熟。
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) — 为 LLM 设计的爬虫，输出干净的 Markdown，天生适合喂 AI。
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) — 把整站抓成 LLM-ready 的 Markdown/结构化数据，带 API。
- [apify/crawlee](https://github.com/apify/crawlee) — Node.js 爬虫与浏览器自动化库，反爬处理完善。
- [microsoft/playwright](https://github.com/microsoft/playwright) — 浏览器自动化标准件，动态页面抓取和 E2E 测试都靠它。
- [browser-use/browser-use](https://github.com/browser-use/browser-use) — 让 AI Agent 直接操控浏览器抓取和操作网页。
- [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) — 自适应反爬的 Python 爬虫库，网站改版也不易失效。
- [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) — 小红书/抖音/B站/微博等中文社媒爬虫合集。
- [NaiboWang/EasySpider](https://github.com/NaiboWang/EasySpider) — 可视化无代码爬虫，图形界面设计采集流程。
- [getmaxun/maxun](https://github.com/getmaxun/maxun) — 开源无代码平台，训练机器人把网页变成 API/表格。
- [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) — Chrome 官方无头浏览器自动化库。
- [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium) — 浏览器自动化元老，跨浏览器兼容性最好。

## 🎨 前端与 UI

让 AI 生成的界面不丑的关键。

- [shadcn-ui/ui](https://github.com/shadcn-ui/ui) — 复制即用的组件集，AI 生成 React 界面的事实标准。
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) — 原子化 CSS，AI 写样式的首选，训练语料最多。
- [saadeghi/daisyui](https://github.com/saadeghi/daisyui) — Tailwind 组件库，纯 class 就能出成品感界面。
- [ant-design/ant-design](https://github.com/ant-design/ant-design) — 企业级 React 组件库，中后台界面直接抄。
- [claude-code · frontend-design 技能](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) — Claude Code 官方前端设计技能，教 AI 做有设计感、不落模板俗套的界面。
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — 一套喂给 AI 的设计语言，让 AI 助手真正懂设计。
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) — 给 AI 装上"审美品味"，不再生成千篇一律的平庸界面。
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 各大品牌设计系统提炼成的 DESIGN.md 合集，丢进项目让 AI 生成风格统一的 UI。
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills) — GSAP 官方 AI 技能，教 AI 正确写动画：最佳实践、常用模式、插件用法。
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) — 一条命令让 AI 克隆任意网站的模板。
- [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) — 用 Claude Code / Codex 生成可直接上线的 Lottie 动画。
- [Web to Figma（Figma 插件）](https://www.figma.com/community/plugin/1297530151115228662/web-to-figma-convert-any-website-or-html-code-to-design) — 把任意网站或 HTML 代码转成 Figma 设计稿。⚠️ 非开源仓库，Figma 社区插件，破例收录。

## 🏗️ 后端与全栈脚手架

在成熟骨架上让 AI 改，比从零生成靠谱得多。

- [fastapi/fastapi](https://github.com/fastapi/fastapi) — Python 高性能 API 框架，类型驱动，AI 生成的代码质量高。
- [nestjs/nest](https://github.com/nestjs/nest) — Node.js 企业级后端框架，结构清晰适合 AI 遵循。
- [supabase/supabase](https://github.com/supabase/supabase) — 开源 Firebase 替代品，数据库+认证+存储一条龙。
- [vercel/next.js](https://github.com/vercel/next.js) — React 全栈框架，AI 最熟悉的前端框架之一。
- [django/django](https://github.com/django/django) — Python 全家桶式 Web 框架，自带 Admin/ORM，AI 语料极多。
- [expressjs/express](https://github.com/expressjs/express) — Node.js 最经典的 Web 框架，简单直接。
- [gin-gonic/gin](https://github.com/gin-gonic/gin) — Go 高性能 Web 框架，写 API 服务的首选。
- [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) — Java 企业级标准，开箱即用。
- [honojs/hono](https://github.com/honojs/hono) — 超轻量 Web 框架，Node/Deno/Bun/Cloudflare Workers 通吃。
- [nuxt/nuxt](https://github.com/nuxt/nuxt) — Vue 全栈框架，Vue 版的 Next.js。
- [prisma/prisma](https://github.com/prisma/prisma) — TypeScript ORM，类型安全的数据库访问层。
- [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) — 单文件后端：数据库+认证+文件存储，一个二进制跑起来。

## 🔌 MCP 与 Agent 生态

给 AI 装外挂的基础设施。

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — MCP 官方服务器合集，文件系统、数据库、搜索等能力即插即用。
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — 社区 MCP 服务器大全，找外挂先来这。
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — 构建有状态多 Agent 应用的框架。
- [microsoft/autogen](https://github.com/microsoft/autogen) — 微软的多 Agent 对话框架。
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — 官方 Playwright MCP，让 AI 直接操控浏览器。
- [github/github-mcp-server](https://github.com/github/github-mcp-server) — GitHub 官方 MCP，让 AI 管理仓库/issue/PR。
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) — 用 Python 快速构建 MCP 服务器和客户端的框架。
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) — 角色分工的多 Agent 协作框架。
- [mem0ai/mem0](https://github.com/mem0ai/mem0) — 给 AI Agent 加一层长期记忆。
- [browserbase/stagehand](https://github.com/browserbase/stagehand) — AI 浏览器自动化框架，自然语言与代码混合控制。
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python) — OpenAI 官方多 Agent 编排 SDK。
- [google/adk-python](https://github.com/google/adk-python) — Google 的 Agent 开发套件（ADK）。

---

## 贡献

欢迎提 PR 收录新仓库，流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。核心要求：达到收录标准 + 一句话说清"对 AI coding 有什么用"。

## License

[CC0-1.0](LICENSE) — 内容随意使用。
