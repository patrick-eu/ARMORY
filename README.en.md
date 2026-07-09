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

- [anthropics/claude-code](https://github.com/anthropics/claude-code) `⭐137k · 2026-07-08` — Terminal-based AI coding agent that understands your whole codebase and executes multi-step tasks.
- [cline/cline](https://github.com/cline/cline) `⭐64.5k · 2026-07-09` — Autonomous coding agent in VS Code: creates/edits files, runs commands, uses the browser.
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) `⭐80.1k · 2026-07-09` — Open-source AI software engineer platform that completes full development tasks.
- [Aider-AI/aider](https://github.com/Aider-AI/aider) `⭐47.2k · 2026-05-22` — Pair programming in your terminal, editing your local git repo directly.
- [continuedev/continue](https://github.com/continuedev/continue) `⭐34.8k · 2026-07-09` — Open-source IDE assistant with customizable models and context sources.
- [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) `⭐24.3k · 2026-05-15` — Community-enhanced fork of Cline with multi-mode agent teams.
- [openai/codex](https://github.com/openai/codex) `⭐96.5k · 2026-07-09` — OpenAI's terminal coding agent, written in Rust, light and fast.
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) `⭐105.9k · 2026-07-09` — Google's open-source terminal AI agent, wired to Gemini.
- [anomalyco/opencode](https://github.com/anomalyco/opencode) `⭐184k · 2026-07-09` — Open-source terminal coding agent; swap in any model you like.
- [aaif-goose/goose](https://github.com/aaif-goose/goose) `⭐50.9k · 2026-07-09` — Local open-source AI agent, extensible for automating engineering tasks.
- [TabbyML/tabby](https://github.com/TabbyML/tabby) `⭐33.7k · 2026-06-30` — Self-hosted AI code completion; the open-source Copilot alternative.
- [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) `⭐25.9k · 2026-07-09` — Open-source VS Code AI agent combining the best of Cline and Roo.

## 📝 Prompts & Rules

Resources for setting rules and stealing inspiration.

- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) `⭐40.3k · 2026-05-30` — Ready-to-use .cursorrules for every stack.
- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) `⭐165.1k · 2026-07-09` — The classic prompt collection; a reference for writing system prompts.
- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) `⭐141.7k · 2026-07-08` — Reverse-engineered system prompts of major AI coding tools; learn how the pros steer models.
- [anthropics/skills](https://github.com/anthropics/skills) `⭐159.7k · 2026-07-01` — Anthropic's official Agent Skills collection; give Claude domain expertise.
- [obra/superpowers](https://github.com/obra/superpowers) `⭐250.4k · 2026-07-06` — A full skill kit for coding agents: brainstorming, TDD, systematic debugging and more.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) `⭐76.3k · 2026-03-11` — The systematic prompt-engineering curriculum: papers, techniques, examples.
- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) `⭐36.9k · 2026-03-01` — Anthropic's official interactive prompt-engineering tutorial.
- [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) `⭐7.7k · 2026-07-04` — Hands-on prompt technique tutorials, basic to advanced, all with code.
- [ai-boost/awesome-prompts](https://github.com/ai-boost/awesome-prompts) `⭐8.4k · 2026-07-09` — Curated prompts from top-rated GPTs plus prompt-engineering resources.

## 📚 Making Code & Docs AI-Readable

Turn repos, web pages, and docs into context an AI can digest.

- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) `⭐15k · 2026-07-08` — One-click conversion of any Git repo into an LLM-friendly text digest.
- [upstash/context7](https://github.com/upstash/context7) `⭐58.8k · 2026-07-09` — MCP server giving the AI live access to up-to-date official docs and code examples.
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) `⭐17.2k · 2026-06-03` — Auto-generates a wiki for any repo, helping both AI and humans understand a project fast.
- [yamadashy/repomix](https://github.com/yamadashy/repomix) `⭐27k · 2026-07-05` — Packs an entire codebase into one AI-friendly file; popular gitingest sibling.
- [microsoft/markitdown](https://github.com/microsoft/markitdown) `⭐164.2k · 2026-06-24` — Microsoft's converter turning Office/PDF and more into LLM-ready Markdown.
- [docling-project/docling](https://github.com/docling-project/docling) `⭐62.9k · 2026-07-09` — IBM's open-source document parser: PDFs, tables, layout, structured output.
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) `⭐74k · 2026-07-09` — High-quality PDF to Markdown/JSON, formulas and tables included.
- [datalab-to/marker](https://github.com/datalab-to/marker) `⭐37.3k · 2026-07-07` — Fast, accurate PDF-to-Markdown with solid formula/table support.
- [jina-ai/reader](https://github.com/jina-ai/reader) `⭐11.5k · 2026-05-22` — Prefix any URL with r.jina.ai and get LLM-friendly body text.
- [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) `⭐15.1k · 2026-07-09` — ETL preprocessing for documents of every format; a RAG-pipeline staple.

## 🕷️ Scraping & Data Collection

- [scrapy/scrapy](https://github.com/scrapy/scrapy) `⭐63k · 2026-07-08` — The veteran Python scraping framework; mature ecosystem the AI knows inside out.
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) `⭐71.6k · 2026-07-08` — A crawler designed for LLMs; outputs clean Markdown, born to be fed to AI.
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) `⭐148.1k · 2026-07-09` — Crawls entire sites into LLM-ready Markdown/structured data, with an API.
- [apify/crawlee](https://github.com/apify/crawlee) `⭐24.6k · 2026-07-09` — Node.js scraping and browser automation library with solid anti-blocking.
- [microsoft/playwright](https://github.com/microsoft/playwright) `⭐92.5k · 2026-07-09` — The standard for browser automation; dynamic-page scraping and E2E testing alike.
- [browser-use/browser-use](https://github.com/browser-use/browser-use) `⭐103.9k · 2026-07-08` — Lets AI agents drive a real browser to scrape and operate web pages.
- [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling) `⭐68.8k · 2026-07-08` — Adaptive anti-blocking Python scraper that survives site redesigns.
- [NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler) `⭐55.9k · 2026-07-09` — Crawler suite for Chinese social media: Xiaohongshu, Douyin, Bilibili, Weibo.
- [NaiboWang/EasySpider](https://github.com/NaiboWang/EasySpider) `⭐44.2k · 2026-07-03` — Visual no-code scraping; design collection flows in a GUI.
- [getmaxun/maxun](https://github.com/getmaxun/maxun) `⭐16.4k · 2026-07-08` — Open-source no-code platform: train robots to turn websites into APIs/spreadsheets.
- [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) `⭐95.3k · 2026-07-09` — Chrome's official headless browser automation library.
- [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium) `⭐34.3k · 2026-07-09` — The browser-automation veteran with the best cross-browser coverage.

## 🎨 Frontend & UI

The key to AI-generated interfaces that don't look terrible.

- [shadcn-ui/ui](https://github.com/shadcn-ui/ui) `⭐118.5k · 2026-07-09` — Copy-paste component collection; the de facto standard for AI-generated React UIs.
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) `⭐95.8k · 2026-07-07` — Utility-first CSS; the AI's first choice for styling, with the most training data.
- [saadeghi/daisyui](https://github.com/saadeghi/daisyui) `⭐41.5k · 2026-07-08` — Tailwind component library; polished interfaces from pure class names.
- [ant-design/ant-design](https://github.com/ant-design/ant-design) `⭐98.6k · 2026-07-09` — Enterprise React component library; admin dashboards ready to copy.
- [claude-code · frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) `⭐137k · 2026-07-08` — Claude Code's official frontend-design skill; teaches the AI intentional, non-templated visual design.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) `⭐44.9k · 2026-07-09` — A design language to feed your AI, making your AI harness genuinely better at design.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) `⭐61k · 2026-07-04` — Gives your AI good taste; stops it from generating boring, generic slop.
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) `⭐98.9k · 2026-06-16` — DESIGN.md files distilled from popular brand design systems; drop one in and let the agent generate a matching UI.
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills) `⭐11.2k · 2026-04-21` — Official AI skills for GSAP: best practices, common animation patterns, plugin usage.
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) `⭐27k · 2026-07-04` — Clone any website with one command using AI coding agents.
- [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) `⭐4.7k · 2026-07-06` — Generate production-ready Lottie animations with Claude Code or Codex.
- [Web to Figma (Figma plugin)](https://www.figma.com/community/plugin/1297530151115228662/web-to-figma-convert-any-website-or-html-code-to-design) — Convert any website or HTML into a Figma design. ⚠️ Not an open-source repo; Figma community plugin, listed as an exception.

## 🏗️ Backend & Full-Stack Scaffolds

Letting the AI modify a proven skeleton beats generating from zero.

- [fastapi/fastapi](https://github.com/fastapi/fastapi) `⭐100.3k · 2026-07-07` — High-performance Python API framework; type-driven, so AI-generated code comes out cleaner.
- [nestjs/nest](https://github.com/nestjs/nest) `⭐76.1k · 2026-07-09` — Enterprise Node.js backend framework with a clear structure that's easy for AI to follow.
- [supabase/supabase](https://github.com/supabase/supabase) `⭐105.9k · 2026-07-09` — Open-source Firebase alternative: database + auth + storage in one.
- [vercel/next.js](https://github.com/vercel/next.js) `⭐140.4k · 2026-07-09` — React full-stack framework; one of the frameworks AI knows best.
- [django/django](https://github.com/django/django) `⭐88k · 2026-07-08` — Batteries-included Python web framework with admin/ORM; massive AI training corpus.
- [expressjs/express](https://github.com/expressjs/express) `⭐69.3k · 2026-07-06` — The classic Node.js web framework; simple and direct.
- [gin-gonic/gin](https://github.com/gin-gonic/gin) `⭐88.9k · 2026-06-26` — High-performance Go web framework; first pick for API services.
- [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) `⭐81.1k · 2026-07-07` — The Java enterprise standard, ready out of the box.
- [honojs/hono](https://github.com/honojs/hono) `⭐31.3k · 2026-07-07` — Ultra-light web framework running on Node/Deno/Bun/Cloudflare Workers alike.
- [nuxt/nuxt](https://github.com/nuxt/nuxt) `⭐60.6k · 2026-07-04` — The Vue full-stack framework; Vue's answer to Next.js.
- [prisma/prisma](https://github.com/prisma/prisma) `⭐46.7k · 2026-07-08` — TypeScript ORM; a type-safe database access layer.
- [pocketbase/pocketbase](https://github.com/pocketbase/pocketbase) `⭐59.5k · 2026-07-08` — Single-file backend: database + auth + file storage in one binary.

## 🔌 MCP & Agent Ecosystem

Infrastructure for giving your AI superpowers.

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) `⭐88.3k · 2026-07-06` — Official MCP server collection: filesystem, databases, search and more, plug and play.
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) `⭐90.5k · 2026-07-04` — The community MCP server directory; start here when hunting for add-ons.
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) `⭐36.9k · 2026-07-09` — Framework for building stateful multi-agent applications.
- [microsoft/autogen](https://github.com/microsoft/autogen) `⭐59.6k · 2026-04-15` — Microsoft's multi-agent conversation framework.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) `⭐34.9k · 2026-06-29` — Official Playwright MCP; let the AI drive a browser directly.
- [github/github-mcp-server](https://github.com/github/github-mcp-server) `⭐31.3k · 2026-07-08` — GitHub's official MCP; let the AI manage repos, issues, PRs.
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) `⭐26.1k · 2026-07-09` — The fast Python framework for building MCP servers and clients.
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) `⭐55.2k · 2026-07-09` — Role-based multi-agent collaboration framework.
- [mem0ai/mem0](https://github.com/mem0ai/mem0) `⭐60.5k · 2026-07-09` — A long-term memory layer for AI agents.
- [browserbase/stagehand](https://github.com/browserbase/stagehand) `⭐23.4k · 2026-07-09` — AI browser automation blending natural language and code control.
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python) `⭐27.8k · 2026-07-09` — OpenAI's official multi-agent orchestration SDK.
- [google/adk-python](https://github.com/google/adk-python) `⭐20.5k · 2026-07-09` — Google's Agent Development Kit (ADK).

---

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Core requirements: meet the inclusion criteria + one sentence on how it helps AI coding.

## License

[CC0-1.0](LICENSE) — use freely.
