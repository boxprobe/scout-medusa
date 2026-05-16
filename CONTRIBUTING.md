# Contributing to scout-medusa

This repo is a demo / staging area for scout-runnable regression test
scenarios against [Medusa](https://github.com/medusajs/medusa). Some of
these scenarios may eventually be contributed upstream to medusajs/medusa
itself; for now they live here.

## Reporting bugs

If the demo doesn't work for you, open an issue with:

- `docker --version` and `docker compose version`
- Output of `bash compose/start.sh` (if compose-related)
- Output of the failing `scout` command (if scout-related)
- Python version (`python --version`)
- OS and architecture

## Adding a new scenario

The scenario file format is documented in
[boxprobe/scout's README](https://github.com/boxprobe/scout#quickstart).
For this repo specifically:

1. Pick the UI scope. Admin scenarios go under `admin/scenarios/`; a
   storefront-scope `store/` directory would house store scenarios when
   we add them.
2. Each scenario lives in `admin/scenarios/<area>/<scenario-name>/` and
   **must contain both files**:
   - `test.py` — the executable scout scenario (the runtime artifact)
   - `spec.md` — the human-readable scenario card (the review artifact)
3. Use **pixel-anchored Locators** in `test.py` — `bbox=(x, y, w, h)`
   capturing the element's on-page position. Don't introduce CSS
   selectors, `data-testid` lookups, or `aria-label` matching as a
   workaround.
4. Write `spec.md` so a reviewer can understand the scenario in 30
   seconds without reading the Python (format below).
5. From within `admin/`, run the scenario against the baseline first:
   `scout run scenarios/<your>` — make sure it produces a clean recording.
6. Run it against the target — make sure any diff it produces is a real
   regression you want surfaced, not noise. If it's noise, add the field
   or endpoint to `admin/diff_ignore.json` in the same PR.

### `spec.md` format

```markdown
---
name: <area>.<scenario-name>
url: <starting URL path>
tags:
- smoke         # or: core, crud, navigation, edge-case, ...
- crud
priority: critical    # or: high, medium, low
---

## Preconditions

- logged_in: False
- page: /login

## Steps

1. Navigate to ...
2. Enter ... in the ... field
3. Click "..." button
...

## Assertions

- **url_match**: ...
- **<other-assertion-kind>**: ...
```

The point of `spec.md` is that scenarios are **engineering artifacts** —
readable by humans, reviewable in PRs, and (when contributed upstream)
parseable by maintainers of the project being tested. test.py without
spec.md is opaque; bbox coordinates don't tell you what the test does.

See [`admin/scenarios/auth/login-and-logout/spec.md`](admin/scenarios/auth/login-and-logout/spec.md)
for a worked example.

### Why pixel-anchored locators only

scout's whole proposition is **deterministic, near-zero-cost regression
detection**: the same scenario file, against the same app, produces the
same trace at $0 per run. That determinism comes from bbox-anchored
element resolution being pure math — not a probabilistic selector match
against a DOM that can change.

A scenario that falls back to `[data-testid="login-btn"]` looks fine until
the next refactor renames the test-id, at which point the test silently
matches a different element (or nothing) and your regression coverage has
a hole you don't see. Scenarios in this repo are the visible evidence that
scout works; we keep them on the bbox-only path.

PRs that include selector-based locators will be asked to convert to
bboxes or be closed. This isn't unfriendly — it's how the demo stays
honest.

## Updating the pinned version pair

To swap baseline / target to a different pair:

1. Pick two `dtc-starter` commits matching the Medusa versions you want.
2. Update `BASELINE_COMMIT` and `TARGET_COMMIT` in `compose/start.sh`.
3. Update the version comments next to each commit hash.
4. Run `bash compose/start.sh` locally and verify both come up.
5. Run all scenarios against both and check the diff report — likely
   you'll need to add new ignore rules to `diff_ignore.json` for changes
   that the new pair introduces but aren't real regressions.
6. Update `README.md` references to the version numbers.
7. Commit and open a PR. Include the diff report HTML (or a screenshot)
   so reviewers can see what changed.

## Adding noise rules

`<scope>/diff_ignore.json` rule types (see [scout's docs](https://github.com/boxprobe/scout)
for the full schema):

- `field_ignore` — fields anywhere in the response body to ignore
  (`updated_at`, `id`, JSONPath expressions like `$.product.handle`)
- `status_only` — endpoints to compare by status code only, not body
- `endpoint_ignore` — endpoints to drop entirely from the diff
- `header_ignore` — response headers to ignore

When adding a rule, include a brief comment in the PR explaining what
real change in Medusa motivated it. The point isn't a clean diff; the
point is a diff that surfaces real regressions and hides genuine noise.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):
`feat:`, `fix:`, `chore:`, `docs:`, `test:`. English, present tense.

## License

By contributing, you agree your contribution is released under the MIT
license, same as the rest of the repo (see [LICENSE](LICENSE)).
