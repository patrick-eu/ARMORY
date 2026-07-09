# Assemble — An Open-Source Arsenal for Easier AI Coding

> A curated, categorized list of high-star, actively maintained open-source repos to feed your AI (Claude Code / Cursor / Copilot…), so vibe coding gets you what you want with less pain.

**English** | [中文](README.md)

[![Link Health](https://github.com/patrick-eu/Assemble/actions/workflows/check.yml/badge.svg)](https://github.com/patrick-eu/Assemble/actions/workflows/check.yml)

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

Enforced automatically by [`check.py`](check.py); GitHub Actions re-checks weekly and failing repos get removed.

---

## 🤖 AI Coding Tools

The agents and assistants that actually write the code.

- [anthropics/claude-code](https://github.com/anthropics/claude-code) — Terminal-based AI coding agent that understands your whole codebase and executes multi-step tasks.
- [cline/cline](https://github.com/cline/cline) — Autonomous coding agent in VS Code: creates/edits files, runs commands, uses the browser.
- [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) — Open-source AI software engineer platform that completes full development tasks.
- [Aider-AI/aider](https://github.com/Aider-AI/aider) — Pair programming in your terminal, editing your local git repo directly.
- [continuedev/continue](https://github.com/continuedev/continue) — Open-source IDE assistant with customizable models and context sources.
- [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) — Community-enhanced fork of Cline with multi-mode agent teams.

## 📝 Prompts & Rules

Resources for setting rules and stealing inspiration.

- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) — Ready-to-use .cursorrules for every stack.
- [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) — The classic prompt collection; a reference for writing system prompts.
- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) — Reverse-engineered system prompts of major AI coding tools; learn how the pros steer models.

## 📚 Making Code & Docs AI-Readable

Turn repos, web pages, and docs into context an AI can digest.

- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) — One-click conversion of any Git repo into an LLM-friendly text digest.
- [upstash/context7](https://github.com/upstash/context7) — MCP server giving the AI live access to up-to-date official docs and code examples.
- [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) — Auto-generates a wiki for any repo, helping both AI and humans understand a project fast.

## 🕷️ Scraping & Data Collection

- [scrapy/scrapy](https://github.com/scrapy/scrapy) — The veteran Python scraping framework; mature ecosystem the AI knows inside out.
- [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) — A crawler designed for LLMs; outputs clean Markdown, born to be fed to AI.
- [mendableai/firecrawl](https://github.com/mendableai/firecrawl) — Crawls entire sites into LLM-ready Markdown/structured data, with an API.
- [apify/crawlee](https://github.com/apify/crawlee) — Node.js scraping and browser automation library with solid anti-blocking.
- [microsoft/playwright](https://github.com/microsoft/playwright) — The standard for browser automation; dynamic-page scraping and E2E testing alike.

## 🎨 Frontend & UI

The key to AI-generated interfaces that don't look terrible.

- [shadcn-ui/ui](https://github.com/shadcn-ui/ui) — Copy-paste component collection; the de facto standard for AI-generated React UIs.
- [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) — Utility-first CSS; the AI's first choice for styling, with the most training data.
- [saadeghi/daisyui](https://github.com/saadeghi/daisyui) — Tailwind component library; polished interfaces from pure class names.
- [ant-design/ant-design](https://github.com/ant-design/ant-design) — Enterprise React component library; admin dashboards ready to copy.
- [claude-code · frontend-design skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md) — Claude Code's official frontend-design skill; teaches the AI intentional, non-templated visual design.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — A design language to feed your AI, making your AI harness genuinely better at design.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) — Gives your AI good taste; stops it from generating boring, generic slop.
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — DESIGN.md files distilled from popular brand design systems; drop one in and let the agent generate a matching UI.
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills) — Official AI skills for GSAP: best practices, common animation patterns, plugin usage.
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) — Clone any website with one command using AI coding agents.
- [diffusionstudio/lottie](https://github.com/diffusionstudio/lottie) — Generate production-ready Lottie animations with Claude Code or Codex.
- [Web to Figma (Figma plugin)](https://www.figma.com/community/plugin/1297530151115228662/web-to-figma-convert-any-website-or-html-code-to-design) — Convert any website or HTML into a Figma design. ⚠️ Not an open-source repo; Figma community plugin, listed as an exception.

## 🏗️ Backend & Full-Stack Scaffolds

Letting the AI modify a proven skeleton beats generating from zero.

- [fastapi/fastapi](https://github.com/fastapi/fastapi) — High-performance Python API framework; type-driven, so AI-generated code comes out cleaner.
- [nestjs/nest](https://github.com/nestjs/nest) — Enterprise Node.js backend framework with a clear structure that's easy for AI to follow.
- [supabase/supabase](https://github.com/supabase/supabase) — Open-source Firebase alternative: database + auth + storage in one.
- [vercel/next.js](https://github.com/vercel/next.js) — React full-stack framework; one of the frameworks AI knows best.

## 🔌 MCP & Agent Ecosystem

Infrastructure for giving your AI superpowers.

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Official MCP server collection: filesystem, databases, search and more, plug and play.
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — The community MCP server directory; start here when hunting for add-ons.
- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — Framework for building stateful multi-agent applications.
- [microsoft/autogen](https://github.com/microsoft/autogen) — Microsoft's multi-agent conversation framework.

---

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Core requirements: meet the inclusion criteria + one sentence on how it helps AI coding.

## License

[CC0-1.0](LICENSE) — use freely.
