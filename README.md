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

标准由 [`check.py`](check.py) 自动校验，GitHub Actions 每周体检一次，不达标的会被移除。每个条目的 `⭐ star 数 · 最后更新日期` 也由 CI 每周自动刷新。

---

## 🤖 AI 编程工具

直接帮你写代码的 Agent / 助手本体。

- [anthropics/claude-code](https://github.com/anthropics/claude-code) `⭐137k · 2026-07-08` — 终端里的 AI 编程 Agent，理解整个代码库，执行多步任务。
- [cline/cline](https://github.com/cline/cline) `⭐64.5k · 2026-07-09` — VS Code 里的自主编程 Agent，能创建/编辑文件、跑命令、用浏览器。
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) `⭐80.1k · 2026-07-09` — 开源 AI 软件工程师平台，能完成完整开发任务。
- [Aider-AI/aider](https://github.com/Aider-AI/aider) `⭐47.2k · 2026-05-22` — 终端结对编程工具，直接在本地 git 仓库上改代码。
- [continuedev/continue](https://github.com/continuedev/continue) `⭐34.8k · 2026-07-09` — 开源 IDE 助手，可自定义模型和上下文源。
- [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) `⭐24.3k · 2026-05-15` — Cline 的社区增强分支，多模式 Agent 团队。
- [openai/codex](https://github.com/openai/codex) `⭐96.5k · 2026-07-09` — OpenAI 的终端编程 Agent，Rust 实现，轻量快速。
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) `⭐105.9k · 2026-07-09` — Google 开源的终端 AI Agent，直连 Gemini。
- [anomalyco/opencode](https://github.com/anomalyco/opencode) `⭐184k · 2026-07-09` — 开源终端 AI 编程 Agent，模型随便换。
- [aaif-goose/goose](https://github.com/aaif-goose/goose) `⭐50.9k · 2026-07-09` — 本地运行的开源 AI Agent，可装扩展自动化工程任务。
- [TabbyML/tabby](https://github.com/TabbyML/tabby) `⭐33.7k · 2026-06-30` — 自托管 AI 代码补全，Copilot 的开源替代。
- [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) `⭐25.9k · 2026-07-09` — VS Code 开源 AI Agent，集 Cline/Roo 之长。

## 📝 提示词与规则

给 AI 定规矩、给灵感的资源库。

- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) `⭐40.3k · 2026-05-30` — 各种技术栈的 .cursorrules 规则合集，拿来即用。
- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) `⭐165.1k · 2026-07-09` — 经典提示词大全，写系统提示词的参考。
- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) `⭐141.7k · 2026-07-08` — 各大 AI 编程工具的系统提示词逆向合集，学习工具怎么"调教"模型。
- [anthropics/skills](https://github.com/anthropics/skills) `⭐159.7k · 2026-07-01` — Anthropic 官方 Agent Skills 合集，给 Claude 装领域技能。
- [obra/superpowers](https://github.com/obra/superpowers) `⭐250.4k · 2026-07-06` — 编程 Agent 技能全家桶：头脑风暴、TDD、系统化调试等工作流。
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) `⭐76.3k · 2026-03-11` — 提示词工程系统教程，论文、技巧、案例俱全。
- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) `⭐37k · 2026-03-01` — Anthropic 官方交互式提示词教程。
- [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) `⭐7.7k · 2026-07-04` — 提示词技术实战教程集，从基础到高级都带代码。
- [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) `⭐8.4k · 2026-07-09` — 精选高分 GPTs 提示词与提示词工程资料。

## 📚 让 AI 读懂代码与文档

把仓库、网页、文档转成 AI 能吃的上下文。

- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) `⭐15k · 2026-07-08` — 把任意 Git 仓库一键变成适合喂给 LLM 的纯文本摘要。
- [upstash/context7](https://github.com/upstash/context7) `⭐58.8k · 2026-07-09` — MCP 服务器，让 AI 实时获取库的最新官方文档和示例代码。
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) `⭐17.2k · 2026-06-03` — 给任意仓库自动生成 Wiki 文档，帮 AI 和人快速理解项目。
- [yamadashy/repomix](https://github.com/yamadashy/repomix) `⭐27k · 2026-07-05` — 把整个代码库打包成一份 AI 友好的文件，gitingest 的热门同类。
- [microsoft/markitdown](https://github.com/microsoft/markitdown) `⭐164.2k · 2026-06-24` — 微软出品，Office/PDF 等各种文件转 Markdown 喂 LLM。
- [docling-project/docling](https://github.com/docling-project/docling) `⭐62.9k · 2026-07-09` — IBM 开源文档解析器，PDF/表格/版面理解，输出结构化数据。
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) `⭐74k · 2026-07-09` — 高质量 PDF 转 Markdown/JSON，公式表格都能抽。
- [datalab-to/marker](https://github.com/datalab-to/marker) `⭐37.3k · 2026-07-07` — PDF 快速精准转 Markdown，公式表格支持好。
- [jina-ai/reader](https://github.com/jina-ai/reader) `⭐11.5k · 2026-05-22` — 任意 URL 前加 r.jina.ai 即得 LLM 友好的正文文本。
- [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) `⭐15.1k · 2026-07-09` — 各种格式文档的 ETL 预处理库，RAG 数据管道常客。

## 🕷️ 爬虫与数据采集

- [scrapy/scrapy](https://github.com/scrapy/scrapy) `⭐63k · 2026-07-08` — Python 爬虫框架老大哥，生态成熟，AI 对它的用法非常熟。
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) `⭐71.6k · 2026-07-08` — 为 LLM 设计的爬虫，输出干净的 Markdown，天生适合喂 AI。
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) `⭐148.1k · 2026-07-09` — 把整站抓成 LLM-ready 的 Markdown/结构化数据，带 API。
- [apify/crawlee](https://github.com/apify/crawlee) `⭐24.6k · 2026-07-09` — Node.js 爬虫与浏览器自动化库，反爬处理完善。
- [microsoft/playwright](https://github.com/microsoft/playwright) `⭐92.5k · 2026-07-09` — 浏览器自动化标准件，动态页面抓取和 E2E 测试都靠它。
- [browser-use/browser-use](https://github.com/browser-use/browser-use) `⭐103.9k · 2026-07-08` — 让 AI Agent 直接操控浏览器抓取和操作网页。
- [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) `⭐68.8k · 2026-07-08` — 自适应反爬的 Python 爬虫库，网站改版也不易失效。
- [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) `⭐55.9k · 2026-07-09` — 小红书/抖音/B站/微博等中文社媒爬虫合集。
- [NaiboWang/EasySpider](https://github.com/NaiboWang/EasySpider) `⭐44.2k · 2026-07-03` — 可视化无代码爬虫，图形界面设计采集流程。
- [getmaxun/maxun](https://github.com/getmaxun/maxun) `⭐16.4k · 2026-07-09` — 开源无代码平台，训练机器人把网页变成 API/表格。
- [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) `⭐95.3k · 2026-07-09` — Chrome 官方无头浏览器自动化库。
- [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium) `⭐34.3k · 2026-07-09` — 浏览器自动化元老，跨浏览器兼容性最好。

## 🎨 前端与 UI

让 AI 生成的界面不丑的关键。

- [shadcn-ui/ui](https://github.com/shadcn-ui/ui) `⭐118.5k · 2026-07-09` — 复制即用的组件集，AI 生成 React 界面的事实标准。
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) `⭐95.8k · 2026-07-07` — 原子化 CSS，AI 写样式的首选，训练语料最多。
- [saadeghi/daisyui](https://github.com/saadeghi/daisyui) `⭐41.5k · 2026-07-08` — Tailwind 组件库，纯 class 就能出成品感界面。
- [ant-design/ant-design](https://github.com/ant-design/ant-design) `⭐98.6k · 2026-07-09` — 企业级 React 组件库，中后台界面直接抄。
- [claude-code · frontend-design 技能](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) `⭐137k · 2026-07-08` — Claude Code 官方前端设计技能，教 AI 做有设计感、不落模板俗套的界面。
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) `⭐44.9k · 2026-07-09` — 一套喂给 AI 的设计语言，让 AI 助手真正懂设计。
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) `⭐61k · 2026-07-04` — 给 AI 装上"审美品味"，不再生成千篇一律的平庸界面。
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) `⭐98.9k · 2026-06-16` — 各大品牌设计系统提炼成的 DESIGN.md 合集，丢进项目让 AI 生成风格统一的 UI。
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills) `⭐11.2k · 2026-04-21` — GSAP 官方 AI 技能，教 AI 正确写动画：最佳实践、常用模式、插件用法。
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) `⭐27.1k · 2026-07-04` — 一条命令让 AI 克隆任意网站的模板。
- [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) `⭐4.7k · 2026-07-06` — 用 Claude Code / Codex 生成可直接上线的 Lottie 动画。
- [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) `⭐1.5k · 2026-06-28` — AI logo 动画技能：把位图 logo 变成流畅的 SVG 动画和 GIF/视频预览。
- [Web to Figma（Figma 插件）](https://www.figma.com/community/plugin/1297530151115228662/web-to-figma-convert-any-website-or-html-code-to-design) — 把任意网站或 HTML 代码转成 Figma 设计稿。⚠️ 非开源仓库，Figma 社区插件，破例收录。

## 🏗️ 后端与全栈脚手架

在成熟骨架上让 AI 改，比从零生成靠谱得多。

- [fastapi/fastapi](https://github.com/fastapi/fastapi) `⭐100.3k · 2026-07-07` — Python 高性能 API 框架，类型驱动，AI 生成的代码质量高。
- [nestjs/nest](https://github.com/nestjs/nest) `⭐76.1k · 2026-07-09` — Node.js 企业级后端框架，结构清晰适合 AI 遵循。
- [supabase/supabase](https://github.com/supabase/supabase) `⭐105.9k · 2026-07-09` — 开源 Firebase 替代品，数据库+认证+存储一条龙。
- [vercel/next.js](https://github.com/vercel/next.js) `⭐140.4k · 2026-07-09` — React 全栈框架，AI 最熟悉的前端框架之一。
- [django/django](https://github.com/django/django) `⭐88k · 2026-07-08` — Python 全家桶式 Web 框架，自带 Admin/ORM，AI 语料极多。
- [expressjs/express](https://github.com/expressjs/express) `⭐69.3k · 2026-07-06` — Node.js 最经典的 Web 框架，简单直接。
- [gin-gonic/gin](https://github.com/gin-gonic/gin) `⭐88.9k · 2026-06-26` — Go 高性能 Web 框架，写 API 服务的首选。
- [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) `⭐81.1k · 2026-07-07` — Java 企业级标准，开箱即用。
- [honojs/hono](https://github.com/honojs/hono) `⭐31.3k · 2026-07-07` — 超轻量 Web 框架，Node/Deno/Bun/Cloudflare Workers 通吃。
- [nuxt/nuxt](https://github.com/nuxt/nuxt) `⭐60.6k · 2026-07-04` — Vue 全栈框架，Vue 版的 Next.js。
- [prisma/prisma](https://github.com/prisma/prisma) `⭐46.7k · 2026-07-08` — TypeScript ORM，类型安全的数据库访问层。
- [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) `⭐59.5k · 2026-07-08` — 单文件后端：数据库+认证+文件存储，一个二进制跑起来。

## ✅ 测试与质量保障

AI 写的代码，得有办法证明它是对的。

- [pytest-dev/pytest](https://github.com/pytest-dev/pytest) `⭐14.3k · 2026-07-07` — Python 测试框架事实标准，插件生态庞大。
- [vitest-dev/vitest](https://github.com/vitest-dev/vitest) `⭐16.8k · 2026-07-09` — Vite 原生测试框架，前端项目开箱即用。
- [jestjs/jest](https://github.com/jestjs/jest) `⭐45.5k · 2026-07-09` — 经典 JS 测试框架，语料最多，AI 最熟。
- [cypress-io/cypress](https://github.com/cypress-io/cypress) `⭐50.4k · 2026-07-09` — 端到端测试框架，在真实浏览器里跑用户流程。
- [astral-sh/ruff](https://github.com/astral-sh/ruff) `⭐48.5k · 2026-07-09` — 极快的 Python linter + 格式化器，AI 生成的代码先过一遍。
- [biomejs/biome](https://github.com/biomejs/biome) `⭐25.3k · 2026-07-09` — JS/TS 一体化 lint + 格式化，Prettier/ESLint 二合一替代。
- [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) `⭐12k · 2026-07-09` — AI 自动 code review，在 PR 里直接给改进建议。
- [faker-js/faker](https://github.com/faker-js/faker) `⭐15.4k · 2026-07-09` — 批量生成逼真的测试数据。
- [locustio/locust](https://github.com/locustio/locust) `⭐28k · 2026-07-09` — 用 Python 脚本写场景的压测工具。
- [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js) `⭐2.9k · 2026-07-09` — 变异测试，检验你的测试是不是真能抓住 bug。

## 🚀 部署与上线

最后一公里：让 AI 照着成熟方案写部署，别自己瞎折腾。

- [coollabsio/coolify](https://github.com/coollabsio/coolify) `⭐58.2k · 2026-07-08` — 自托管的 Vercel/Heroku 替代，点几下把应用跑起来。
- [Dokploy/dokploy](https://github.com/Dokploy/dokploy) `⭐35.5k · 2026-07-09` — 开源部署面板，Docker 应用一键上线。
- [caddyserver/caddy](https://github.com/caddyserver/caddy) `⭐73.9k · 2026-07-08` — 自动 HTTPS 的 Web 服务器，配置极简。
- [NginxProxyManager/nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager) `⭐33.5k · 2026-06-29` — 图形界面管理 Nginx 反代和证书。
- [docker/compose](https://github.com/docker/compose) `⭐37.7k · 2026-07-09` — 多容器应用编排的标准件。
- [traefik/traefik](https://github.com/traefik/traefik) `⭐63.9k · 2026-07-09` — 云原生反向代理，服务发现全自动。
- [portainer/portainer](https://github.com/portainer/portainer) `⭐37.9k · 2026-07-07` — Docker/K8s 图形化管理面板。
- [cloudflare/cloudflared](https://github.com/cloudflare/cloudflared) `⭐14.8k · 2026-07-08` — Cloudflare Tunnel 客户端，把内网服务安全暴露到公网。
- [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) `⭐88.9k · 2026-07-09` — 自托管可用性监控，服务挂了立刻知道。
- [getsentry/sentry](https://github.com/getsentry/sentry) `⭐44.2k · 2026-07-09` — 错误追踪与性能监控，上线后第一时间发现问题。

## ⚙️ 自动化与工作流

很多需求本质是"自动化个流程"——先看看有没有现成积木。

- [n8n-io/n8n](https://github.com/n8n-io/n8n) `⭐195.8k · 2026-07-09` — 可视化工作流自动化平台，几百个集成节点。
- [activepieces/activepieces](https://github.com/activepieces/activepieces) `⭐23.2k · 2026-07-09` — 开源 Zapier 替代，AI 也能当节点用。
- [windmill-labs/windmill](https://github.com/windmill-labs/windmill) `⭐17.1k · 2026-07-09` — 把脚本变成工作流和 UI 的开发者平台，多语言支持。
- [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) `⭐15.6k · 2026-07-09` — 代码优先的后台任务/工作流框架。
- [temporalio/temporal](https://github.com/temporalio/temporal) `⭐21.5k · 2026-07-09` — 可靠执行长流程的工作流引擎，失败自动恢复。
- [apache/airflow](https://github.com/apache/airflow) `⭐46.1k · 2026-07-09` — 数据管道调度的老牌标准。
- [kestra-io/kestra](https://github.com/kestra-io/kestra) `⭐27.3k · 2026-07-09` — 声明式（YAML）编排平台，事件驱动。
- [huginn/huginn](https://github.com/huginn/huginn) `⭐49.6k · 2026-07-09` — 自托管版"IFTTT"，一群 agent 帮你盯网页、发通知。

## 🎬 视频制作

让 AI 帮你剪片、出片、做动画。

- [browser-use/video-use](https://github.com/browser-use/video-use) `⭐16.2k · 2026-07-01` — 用编程 Agent 剪视频，视频界的 browser-use。
- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) `⭐35.9k · 2026-07-09` — 开源 Agent 化视频生产系统：12 条流水线、500+ 技能，把 AI 编程助手变成视频工作室。
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) `⭐96.4k · 2026-07-09` — 给个主题就自动生成短视频，文案配音字幕全流程 AI。
- [remotion-dev/remotion](https://github.com/remotion-dev/remotion) `⭐52.6k · 2026-07-09` — 用 React 写视频，AI 生成组件代码即可出片。
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) `⭐61.9k · 2026-06-21` — 开源网页版视频剪辑器，CapCut 的替代品。
- [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) `⭐61.9k · 2026-07-09` — 音视频处理的万能底座，AI 写 ffmpeg 命令非常熟。
- [Zulko/moviepy](https://github.com/Zulko/moviepy) `⭐14.8k · 2026-03-07` — Python 脚本化视频剪辑库，让 AI 生成剪辑脚本的首选。
- [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas) `⭐18.8k · 2026-07-02` — 用 TS 代码写程序化动画，带可视化预览编辑。
- [midrender/revideo](https://github.com/midrender/revideo) `⭐3.9k · 2026-07-07` — 代码生成视频的 TypeScript 框架，主打自动化出片。
- [ManimCommunity/manim](https://github.com/ManimCommunity/manim) `⭐39.4k · 2026-07-08` — 3Blue1Brown 同款数学动画引擎，做讲解视频的利器。
- [mifi/lossless-cut](https://github.com/mifi/lossless-cut) `⭐42k · 2026-06-22` — 无损快速剪切视频，不重新编码秒级出片。

## 🔌 MCP 与 Agent 生态

给 AI 装外挂的基础设施。

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) `⭐88.3k · 2026-07-06` — MCP 官方服务器合集，文件系统、数据库、搜索等能力即插即用。
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) `⭐90.5k · 2026-07-04` — 社区 MCP 服务器大全，找外挂先来这。
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) `⭐36.9k · 2026-07-09` — 构建有状态多 Agent 应用的框架。
- [microsoft/autogen](https://github.com/microsoft/autogen) `⭐59.6k · 2026-04-15` — 微软的多 Agent 对话框架。
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) `⭐34.9k · 2026-06-29` — 官方 Playwright MCP，让 AI 直接操控浏览器。
- [github/github-mcp-server](https://github.com/github/github-mcp-server) `⭐31.3k · 2026-07-09` — GitHub 官方 MCP，让 AI 管理仓库/issue/PR。
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) `⭐26.1k · 2026-07-09` — 用 Python 快速构建 MCP 服务器和客户端的框架。
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) `⭐55.2k · 2026-07-09` — 角色分工的多 Agent 协作框架。
- [mem0ai/mem0](https://github.com/mem0ai/mem0) `⭐60.5k · 2026-07-09` — 给 AI Agent 加一层长期记忆。
- [browserbase/stagehand](https://github.com/browserbase/stagehand) `⭐23.4k · 2026-07-09` — AI 浏览器自动化框架，自然语言与代码混合控制。
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python) `⭐27.8k · 2026-07-09` — OpenAI 官方多 Agent 编排 SDK。
- [google/adk-python](https://github.com/google/adk-python) `⭐20.5k · 2026-07-09` — Google 的 Agent 开发套件（ADK）。

---

## 贡献

欢迎提 PR 收录新仓库，流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。核心要求：达到收录标准 + 一句话说清"对 AI coding 有什么用"。

## License

[CC0-1.0](LICENSE) — 内容随意使用。
