# Profile README editing contract

This repository is the **public GitHub profile** for `@eusouakell`. Its `README.md` is a designed, human-facing landing page, **not** an automatically synchronized repository catalog or changelog.

## Canonical presentation (preserve on every update)

1. Start with the existing banner and a short **first-person positioning story** linking marketing, UX/content design, knowledge work and Context Engineering. Prefer voice and evidence over tool inventories.
2. Keep **five visual expertise badges** (Context Engineering, Marketing Strategy, Knowledge Architecture, Agent Skills, Responsible AI), the **positioning-path** illustration, **three linked credential images** and the visual social/action badges.
3. Show no more than **four to five selected project items**, each a single concise line. Send exhaustive information, statuses, architecture details and benchmarks to `PROJECTS.md`, `CREDENTIALS.md` and project repositories. Do not turn the profile into a long project matrix.
4. Preserve the explicit provenance of the **Bússola** group project and credit the original technical implementation to **Victor Lopes / theguitarvity**. Preserve attribution for outside forks and third-party resources where they are mentioned.
5. Link only to verified assets, projects and credentials. Label research as research and avoid unsupported benchmark, certification, partnership or authorship claims.
6. Keep a **compact, scannable** page, with short paragraphs, whitespace, no large tables, no badges generated from unverified claims and no accumulation of redundant sections. Reference visual baseline: commit `945de72c` (2026-10-01).

## Mandatory update protocol

1. **Inspect the current README and this contract** before writing. Compare against the visual baseline and recent history.
2. Limit modifications to the smallest relevant paragraph/project. An unrelated repository, issue or credential update **does not authorize a complete README rewrite**.
3. Before changing a protected visual element (banner, expertise badges, linked credential gallery, positioning illustration, links to public work), explain the reason and obtain explicit **human approval** for the design change.
4. Make changes on a branch and open a PR; **do not push directly to main or merge automatically**. Include a before/after summary for positioning, badges, visuals, project references and provenance.
5. Run `python3 scripts/profile_readme_guard.py` and inspect the GitHub-rendered README in desktop and mobile. A passing guard does not replace human visual approval.
6. If a new project is worthy of the profile, **replace a lower-priority item** instead of appending indefinitely. If a detail is lengthy, update `PROJECTS.md` and link to it.

This contract applies to human edits, Codex, Copilot and any connected agent/automation with repository write permission. A workflow that cannot follow it must **stop and open an issue/PR proposal**, not overwrite the page.
