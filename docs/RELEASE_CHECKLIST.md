# Public-release checklist

This repository is a local independent Git repository. The experiment outputs
under `runs/` are intentionally ignored and must be selectively exported only
after removing credentials, private paths, and any non-redistributable source
content.

## Before public release

- [x] Choose and add Apache-2.0 for original code and documentation.
- [ ] Confirm that AgentDojo/OpenClaw source terms permit the intended artifact
      references and that no source case content is redistributed without
      permission.
- [x] Remove absolute local paths from public manifests where a relative path
      or hash is sufficient.
- [x] Verify that no API key, dotenv file, token, session transcript, or private
      workspace file is staged.
- [ ] Export only sanitized outcome-complete cases and deterministic summaries.
- [x] Run the repository tests and `git diff --check` on the release commit.
- [x] Ask for explicit confirmation before creating a remote GitHub repository,
      pushing commits, or enabling public visibility.

## Current local state

- Repository: `taam-openclaw`
- Remote: `https://github.com/helloswx/taam-openclaw.git`
- DeepSeek pilot log: `docs/DEEPSEEK_PILOT_LOG.md`
- Registered DeepSeek baseline: `configs/deepseek-phase1-v1.json`
- Victim outputs: local-only under `runs/` and ignored by Git

The public repository was created after explicit user confirmation and the
reviewed `main` branch was pushed. Raw campaign outputs remain local until a
separate, sanitized data-release decision is made.
