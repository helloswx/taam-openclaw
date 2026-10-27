# Public-release checklist

This repository is a local independent Git repository. The experiment outputs
under `runs/` are intentionally ignored and must be selectively exported only
after removing credentials, private paths, and any non-redistributable source
content.

## Before public release

- [ ] Choose and add a license for original code and documentation.
- [ ] Confirm that AgentDojo/OpenClaw source terms permit the intended artifact
      references and that no source case content is redistributed without
      permission.
- [ ] Remove absolute local paths from public manifests where a relative path
      or hash is sufficient.
- [ ] Verify that no API key, dotenv file, token, session transcript, or private
      workspace file is staged.
- [ ] Export only sanitized outcome-complete cases and deterministic summaries.
- [ ] Run the repository tests and `git diff --check` on the release commit.
- [ ] Ask for explicit confirmation before creating a remote GitHub repository,
      pushing commits, or enabling public visibility.

## Current local state

- Repository: `taam-openclaw`
- Remote: none configured
- DeepSeek pilot log: `docs/DEEPSEEK_PILOT_LOG.md`
- Registered DeepSeek baseline: `configs/deepseek-phase1-v1.json`
- Victim outputs: local-only under `runs/` and ignored by Git
