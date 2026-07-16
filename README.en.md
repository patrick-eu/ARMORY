# ARMORY — An Open-Source Arsenal for Easier AI Coding

> A curated, categorized list of high-star, actively maintained open-source repos to feed your AI (Claude Code / Cursor / Copilot…), so vibe coding gets you what you want with less pain.

**English** | [中文](README.md)

[![Link Health](https://github.com/patrick-eu/ARMORY/actions/workflows/check.yml/badge.svg)](https://github.com/patrick-eu/ARMORY/actions/workflows/check.yml)

## How to use

Common ways to "feed" these repos to your AI:

1. **Just give it the link**: ask the AI to build on top of a listed repo, e.g. "use crawl4ai to write a scraper for XX".
2. **Turn repos into context**: use [gitingest](https://github.com/coderamp-labs/gitingest) to flatten an entire repo into plain text and paste it in.
3. **Plug in MCP**: use MCP servers like [context7](https://github.com/upstash/context7) so the AI reads up-to-date docs instead of stale memory.
4. **Copy a template**: clone a listed scaffold and let the AI modify a proven skeleton instead of hallucinating from scratch.

## Inclusion criteria

To keep out malicious and abandoned code, every listed repo must satisfy all of:

- ⭐ **≥ 1000 stars**
- 🔄 **committed to within the last 6 months**
- 📄 **a clear open-source license**

Enforced automatically by [`check.py`](check.py); GitHub Actions re-checks weekly and failing repos get removed. Each entry's `⭐ stars · last-updated date` badge is also refreshed weekly by CI.

---

## 🤖 AI Coding Tools

The agents and assistants that actually write the code.

- [anthropics/claude-code](https://github.com/anthropics/claude-code) `⭐138.1k · 2026-07-15` — Terminal-based AI coding agent that understands your whole codebase and executes multi-step tasks.
- [cline/cline](https://github.com/cline/cline) `⭐64.7k · 2026-07-16` — Autonomous coding agent in VS Code: creates/edits files, runs commands, uses the browser.
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) `⭐81k · 2026-07-16` — Open-source AI software engineer platform that completes full development tasks.
- [Aider-AI/aider](https://github.com/Aider-AI/aider) `⭐47.4k · 2026-05-22` — Pair programming in your terminal, editing your local git repo directly.
- [continuedev/continue](https://github.com/continuedev/continue) `⭐34.9k · 2026-07-16` — Open-source IDE assistant with customizable models and context sources.
- [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) `⭐24.3k · 2026-05-15` — Community-enhanced fork of Cline with multi-mode agent teams.
- [openai/codex](https://github.com/openai/codex) `⭐98.7k · 2026-07-16` — OpenAI's terminal coding agent, written in Rust, light and fast.
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) `⭐106k · 2026-07-16` — Google's open-source terminal AI agent, wired to Gemini.
- [anomalyco/opencode](https://github.com/anomalyco/opencode) `⭐186.4k · 2026-07-16` — Open-source terminal coding agent; swap in any model you like.
- [aaif-goose/goose](https://github.com/aaif-goose/goose) `⭐51.3k · 2026-07-16` — Local open-source AI agent, extensible for automating engineering tasks.
- [TabbyML/tabby](https://github.com/TabbyML/tabby) `⭐33.7k · 2026-06-30` — Self-hosted AI code completion; the open-source Copilot alternative.
- [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) `⭐26.3k · 2026-07-16` — Open-source VS Code AI agent combining the best of Cline and Roo.

## 📝 Prompts & Rules

Resources for setting rules and stealing inspiration.

- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) `⭐40.3k · 2026-05-30` — Ready-to-use .cursorrules for every stack.
- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) `⭐165.8k · 2026-07-16` — The classic prompt collection; a reference for writing system prompts.
- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) `⭐142k · 2026-07-12` — Reverse-engineered system prompts of major AI coding tools; learn how the pros steer models.
- [anthropics/skills](https://github.com/anthropics/skills) `⭐161.6k · 2026-07-13` — Anthropic's official Agent Skills collection; give Claude domain expertise.
- [obra/superpowers](https://github.com/obra/superpowers) `⭐255.8k · 2026-07-16` — A full skill kit for coding agents: brainstorming, TDD, systematic debugging and more.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) `⭐76.5k · 2026-03-11` — The systematic prompt-engineering curriculum: papers, techniques, examples.
- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) `⭐37.1k · 2026-03-01` — Anthropic's official interactive prompt-engineering tutorial.
- [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) `⭐7.7k · 2026-07-14` — Hands-on prompt technique tutorials, basic to advanced, all with code.
- [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) `⭐8.5k · 2026-07-16` — Curated prompts from top-rated GPTs plus prompt-engineering resources.

## 📚 Making Code & Docs AI-Readable

Turn repos, web pages, and docs into context an AI can digest.

- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) `⭐15.1k · 2026-07-14` — One-click conversion of any Git repo into an LLM-friendly text digest.
- [upstash/context7](https://github.com/upstash/context7) `⭐59.2k · 2026-07-13` — MCP server giving the AI live access to up-to-date official docs and code examples.
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) `⭐17.3k · 2026-06-03` — Auto-generates a wiki for any repo, helping both AI and humans understand a project fast.
- [yamadashy/repomix](https://github.com/yamadashy/repomix) `⭐27.2k · 2026-07-15` — Packs an entire codebase into one AI-friendly file; popular gitingest sibling.
- [microsoft/markitdown](https://github.com/microsoft/markitdown) `⭐166.5k · 2026-06-24` — Microsoft's converter turning Office/PDF and more into LLM-ready Markdown.
- [docling-project/docling](https://github.com/docling-project/docling) `⭐63.3k · 2026-07-15` — IBM's open-source document parser: PDFs, tables, layout, structured output.
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) `⭐74.8k · 2026-07-15` — High-quality PDF to Markdown/JSON, formulas and tables included.
- [datalab-to/marker](https://github.com/datalab-to/marker) `⭐37.5k · 2026-07-07` — Fast, accurate PDF-to-Markdown with solid formula/table support.
- [jina-ai/reader](https://github.com/jina-ai/reader) `⭐11.6k · 2026-05-22` — Prefix any URL with r.jina.ai and get LLM-friendly body text.
- [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) `⭐15.1k · 2026-07-15` — ETL preprocessing for documents of every format; a RAG-pipeline staple.

## 🕷️ Scraping & Data Collection

- [scrapy/scrapy](https://github.com/scrapy/scrapy) `⭐63.2k · 2026-07-13` — The veteran Python scraping framework; mature ecosystem the AI knows inside out.
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) `⭐72.9k · 2026-07-15` — A crawler designed for LLMs; outputs clean Markdown, born to be fed to AI.
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) `⭐151.8k · 2026-07-16` — Crawls entire sites into LLM-ready Markdown/structured data, with an API.
- [apify/crawlee](https://github.com/apify/crawlee) `⭐24.7k · 2026-07-16` — Node.js scraping and browser automation library with solid anti-blocking.
- [microsoft/playwright](https://github.com/microsoft/playwright) `⭐93k · 2026-07-16` — The standard for browser automation; dynamic-page scraping and E2E testing alike.
- [browser-use/browser-use](https://github.com/browser-use/browser-use) `⭐105k · 2026-07-15` — Lets AI agents drive a real browser to scrape and operate web pages.
- [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) `⭐69.7k · 2026-07-15` — Adaptive anti-blocking Python scraper that survives site redesigns.
- [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) `⭐56.7k · 2026-07-16` — Crawler suite for Chinese social media: Xiaohongshu, Douyin, Bilibili, Weibo.
- [NaiboWang/EasySpider](https://github.com/NaiboWang/EasySpider) `⭐44.2k · 2026-07-03` — Visual no-code scraping; design collection flows in a GUI.
- [getmaxun/maxun](https://github.com/getmaxun/maxun) `⭐16.5k · 2026-07-15` — Open-source no-code platform: train robots to turn websites into APIs/spreadsheets.
- [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) `⭐95.5k · 2026-07-16` — Chrome's official headless browser automation library.
- [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium) `⭐34.3k · 2026-07-16` — The browser-automation veteran with the best cross-browser coverage.

## 🎨 Frontend & UI

The key to AI-generated interfaces that don't look terrible.

- [shadcn-ui/ui](https://github.com/shadcn-ui/ui) `⭐119.3k · 2026-07-16` — Copy-paste component collection; the de facto standard for AI-generated React UIs.
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) `⭐96k · 2026-07-16` — Utility-first CSS; the AI's first choice for styling, with the most training data.
- [saadeghi/daisyui](https://github.com/saadeghi/daisyui) `⭐41.7k · 2026-07-12` — Tailwind component library; polished interfaces from pure class names.
- [ant-design/ant-design](https://github.com/ant-design/ant-design) `⭐98.7k · 2026-07-16` — Enterprise React component library; admin dashboards ready to copy.
- [claude-code · frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) `⭐138.1k · 2026-07-15` — Claude Code's official frontend-design skill; teaches the AI intentional, non-templated visual design.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) `⭐47.2k · 2026-07-16` — A design language to feed your AI, making your AI harness genuinely better at design.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) `⭐64.1k · 2026-07-04` — Gives your AI good taste; stops it from generating boring, generic slop.
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) `⭐102.3k · 2026-06-16` — DESIGN.md files distilled from popular brand design systems; drop one in and let the agent generate a matching UI.
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills) `⭐11.6k · 2026-04-21` — Official AI skills for GSAP: best practices, common animation patterns, plugin usage.
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) `⭐28.5k · 2026-07-04` — Clone any website with one command using AI coding agents.
- [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) `⭐4.8k · 2026-07-06` — Generate production-ready Lottie animations with Claude Code or Codex.
- [nolangz/pixel2motion](https://github.com/nolangz/pixel2motion) `⭐1.7k · 2026-07-10` — AI logo-animation skill: turn raster logos into smooth SVG animations with GIF/video previews.
- [emilkowalski/skills · apple-design](https://github.com/emilkowalski/skills/blob/main/skills/apple-design/SKILL.md) `⭐14.1k · 2026-07-15` — Apple-design skill by design engineer Emil Kowalski (of sonner/vaul); teaches the AI Apple-grade motion and detail.
- [Web to Figma (Figma plugin)](https://www.figma.com/community/plugin/1297530151115228662/web-to-figma-convert-any-website-or-html-code-to-design) — Convert any website or HTML into a Figma design. ⚠️ Not an open-source repo; Figma community plugin, listed as an exception.

## 🏗️ Backend & Full-Stack Scaffolds

Letting the AI modify a proven skeleton beats generating from zero.

- [fastapi/fastapi](https://github.com/fastapi/fastapi) `⭐100.6k · 2026-07-16` — High-performance Python API framework; type-driven, so AI-generated code comes out cleaner.
- [nestjs/nest](https://github.com/nestjs/nest) `⭐76.3k · 2026-07-16` — Enterprise Node.js backend framework with a clear structure that's easy for AI to follow.
- [supabase/supabase](https://github.com/supabase/supabase) `⭐106.5k · 2026-07-16` — Open-source Firebase alternative: database + auth + storage in one.
- [vercel/next.js](https://github.com/vercel/next.js) `⭐141.1k · 2026-07-16` — React full-stack framework; one of the frameworks AI knows best.
- [django/django](https://github.com/django/django) `⭐88.2k · 2026-07-15` — Batteries-included Python web framework with admin/ORM; massive AI training corpus.
- [expressjs/express](https://github.com/expressjs/express) `⭐69.4k · 2026-07-12` — The classic Node.js web framework; simple and direct.
- [gin-gonic/gin](https://github.com/gin-gonic/gin) `⭐88.9k · 2026-06-26` — High-performance Go web framework; first pick for API services.
- [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) `⭐81.2k · 2026-07-16` — The Java enterprise standard, ready out of the box.
- [honojs/hono](https://github.com/honojs/hono) `⭐31.4k · 2026-07-16` — Ultra-light web framework running on Node/Deno/Bun/Cloudflare Workers alike.
- [nuxt/nuxt](https://github.com/nuxt/nuxt) `⭐60.8k · 2026-07-16` — The Vue full-stack framework; Vue's answer to Next.js.
- [prisma/prisma](https://github.com/prisma/prisma) `⭐47.4k · 2026-07-16` — TypeScript ORM; a type-safe database access layer.
- [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) `⭐59.8k · 2026-07-16` — Single-file backend: database + auth + file storage in one binary.

## ✅ Testing & Quality

AI-written code needs a way to prove itself correct.

- [pytest-dev/pytest](https://github.com/pytest-dev/pytest) `⭐14.3k · 2026-07-14` — The de facto Python testing framework with a huge plugin ecosystem.
- [vitest-dev/vitest](https://github.com/vitest-dev/vitest) `⭐16.8k · 2026-07-16` — Vite-native testing framework; works out of the box for frontend projects.
- [jestjs/jest](https://github.com/jestjs/jest) `⭐45.5k · 2026-07-15` — The classic JS testing framework; the one AI knows best.
- [cypress-io/cypress](https://github.com/cypress-io/cypress) `⭐50.7k · 2026-07-16` — End-to-end testing that runs user flows in a real browser.
- [astral-sh/ruff](https://github.com/astral-sh/ruff) `⭐48.6k · 2026-07-16` — Blazing-fast Python linter + formatter; run AI output through it first.
- [biomejs/biome](https://github.com/biomejs/biome) `⭐25.4k · 2026-07-16` — All-in-one JS/TS lint + format; a Prettier/ESLint two-in-one replacement.
- [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent) `⭐12.1k · 2026-07-10` — AI-powered code review with suggestions right in the PR.
- [faker-js/faker](https://github.com/faker-js/faker) `⭐15.4k · 2026-07-16` — Generate realistic test data in bulk.
- [locustio/locust](https://github.com/locustio/locust) `⭐28k · 2026-07-14` — Load testing with scenarios scripted in Python.
- [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js) `⭐2.9k · 2026-07-15` — Mutation testing: verify your tests actually catch bugs.

## 🚀 Deployment & Shipping

The last mile: have the AI copy proven deployment setups instead of improvising.

- [coollabsio/coolify](https://github.com/coollabsio/coolify) `⭐58.7k · 2026-07-16` — Self-hosted Vercel/Heroku alternative; apps running in a few clicks.
- [Dokploy/dokploy](https://github.com/Dokploy/dokploy) `⭐35.7k · 2026-07-15` — Open-source deployment panel; one-click shipping for Docker apps.
- [caddyserver/caddy](https://github.com/caddyserver/caddy) `⭐74.1k · 2026-07-15` — Web server with automatic HTTPS and minimal config.
- [NginxProxyManager/nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager) `⭐33.6k · 2026-07-16` — GUI for managing Nginx reverse proxies and certificates.
- [docker/compose](https://github.com/docker/compose) `⭐37.8k · 2026-07-16` — The standard for multi-container app orchestration.
- [traefik/traefik](https://github.com/traefik/traefik) `⭐64k · 2026-07-16` — Cloud-native reverse proxy with automatic service discovery.
- [portainer/portainer](https://github.com/portainer/portainer) `⭐38k · 2026-07-15` — Visual management panel for Docker/K8s.
- [cloudflare/cloudflared](https://github.com/cloudflare/cloudflared) `⭐14.9k · 2026-07-15` — Cloudflare Tunnel client; expose local services to the internet safely.
- [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) `⭐89.2k · 2026-07-16` — Self-hosted uptime monitoring; know the moment a service goes down.
- [getsentry/sentry](https://github.com/getsentry/sentry) `⭐44.3k · 2026-07-16` — Error tracking and performance monitoring; catch problems right after launch.

## ⚙️ Automation & Workflows

Many requests boil down to "automate this flow" — check for ready-made building blocks first.

- [n8n-io/n8n](https://github.com/n8n-io/n8n) `⭐196.6k · 2026-07-16` — Visual workflow automation platform with hundreds of integrations.
- [activepieces/activepieces](https://github.com/activepieces/activepieces) `⭐23.3k · 2026-07-16` — Open-source Zapier alternative; AI can be a node too.
- [windmill-labs/windmill](https://github.com/windmill-labs/windmill) `⭐17.2k · 2026-07-16` — Turn scripts into workflows and UIs; polyglot developer platform.
- [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) `⭐15.7k · 2026-07-16` — Code-first background jobs and workflow framework.
- [temporalio/temporal](https://github.com/temporalio/temporal) `⭐21.7k · 2026-07-16` — Workflow engine for reliably executing long-running processes with auto-recovery.
- [apache/airflow](https://github.com/apache/airflow) `⭐46.1k · 2026-07-16` — The veteran standard for data-pipeline scheduling.
- [kestra-io/kestra](https://github.com/kestra-io/kestra) `⭐27.4k · 2026-07-16` — Declarative (YAML) event-driven orchestration platform.
- [huginn/huginn](https://github.com/huginn/huginn) `⭐49.6k · 2026-07-12` — Self-hosted "IFTTT": a fleet of agents watching pages and sending alerts for you.

## 🎬 Video Production

Let the AI cut, render, and animate for you.

- [browser-use/video-use](https://github.com/browser-use/video-use) `⭐17k · 2026-07-01` — Edit videos with coding agents; browser-use for video.
- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) `⭐39.1k · 2026-07-12` — Open-source agentic video production system: 12 pipelines, 500+ skills, turning your coding assistant into a video studio.
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) `⭐97.8k · 2026-07-16` — Give it a topic and get a finished short video: script, voiceover, subtitles, all AI.
- [remotion-dev/remotion](https://github.com/remotion-dev/remotion) `⭐53.4k · 2026-07-16` — Write videos in React; AI-generated components become rendered footage.
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) `⭐73.5k · 2026-07-10` — Open-source web video editor; the CapCut alternative.
- [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) `⭐62.1k · 2026-07-16` — The universal audio/video foundation; AI knows ffmpeg commands inside out.
- [Zulko/moviepy](https://github.com/Zulko/moviepy) `⭐14.8k · 2026-03-07` — Scripted video editing in Python; the go-to for AI-generated edit scripts.
- [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas) `⭐18.8k · 2026-07-02` — Programmatic animations in TypeScript with a visual preview editor.
- [midrender/revideo](https://github.com/midrender/revideo) `⭐3.9k · 2026-07-15` — TypeScript framework for generating video with code, built for automation.
- [ManimCommunity/manim](https://github.com/ManimCommunity/manim) `⭐39.5k · 2026-07-14` — The 3Blue1Brown-style math animation engine; perfect for explainer videos.
- [mifi/lossless-cut](https://github.com/mifi/lossless-cut) `⭐42.1k · 2026-07-14` — Lossless, instant video cutting with no re-encoding.

## 🔌 MCP & Agent Ecosystem

Infrastructure for giving your AI superpowers.

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) `⭐88.5k · 2026-07-10` — Official MCP server collection: filesystem, databases, search and more, plug and play.
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) `⭐90.8k · 2026-07-13` — The community MCP server directory; start here when hunting for add-ons.
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) `⭐37.4k · 2026-07-15` — Framework for building stateful multi-agent applications.
- [microsoft/autogen](https://github.com/microsoft/autogen) `⭐59.8k · 2026-04-15` — Microsoft's multi-agent conversation framework.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) `⭐35.2k · 2026-07-15` — Official Playwright MCP; let the AI drive a browser directly.
- [github/github-mcp-server](https://github.com/github/github-mcp-server) `⭐31.5k · 2026-07-16` — GitHub's official MCP; let the AI manage repos, issues, PRs.
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) `⭐26.2k · 2026-07-16` — The fast Python framework for building MCP servers and clients.
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) `⭐55.6k · 2026-07-15` — Role-based multi-agent collaboration framework.
- [mem0ai/mem0](https://github.com/mem0ai/mem0) `⭐61k · 2026-07-16` — A long-term memory layer for AI agents.
- [browserbase/stagehand](https://github.com/browserbase/stagehand) `⭐23.5k · 2026-07-16` — AI browser automation blending natural language and code control.
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python) `⭐27.9k · 2026-07-16` — OpenAI's official multi-agent orchestration SDK.
- [google/adk-python](https://github.com/google/adk-python) `⭐20.6k · 2026-07-16` — Google's Agent Development Kit (ADK).

---

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Core requirements: meet the inclusion criteria + one sentence on how it helps AI coding.

## License

[CC0-1.0](LICENSE) — use freely.
