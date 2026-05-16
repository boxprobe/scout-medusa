# scout-medusa

A reproducible scout demo against [Medusa](https://github.com/medusajs/medusa) —
two real versions of the platform side by side, 15 admin-flow scenarios, one
HTML diff report showing what their API changed between the two.

Clone this repo, run docker compose, run scout twice, open the report.

```
boxprobe/scout-medusa
├── compose/         Medusa baseline (v2.13.6) + target (v2.14.0) on Docker
├── scenarios/       15 admin scenarios (auth, customers, inventory, ...)
├── app.json         Default URLs and viewport for the demo
└── diff_ignore.json Suppression rules for known noise (timestamps, IDs, ...)
```

---

## What you'll see

After running the steps below, scout produces an HTML report grouped by
endpoint and user flow:

- **921 API endpoints** captured across 15 scenarios
- **Cross-version diffs** of status codes, response shape, and values
- **Filtered noise** — timestamps, IDs, and other known-changes hidden
- **0 unhandled regressions** for the 2.13.6 → 2.14.0 pair (Medusa shipped
  a clean release here; the demo is calibrated to that ground truth)

You're seeing what a scout regression suite looks like *running against a
real upstream OSS project*, not against a toy example we wrote ourselves.

---

## Prerequisites

| Tool | Version | What for |
|---|---|---|
| Docker + `docker compose` | recent | run baseline + target Medusa |
| Python | ≥ 3.11 | run scout |
| `pip` (or `uv`) | recent | install scout |

10-15 GB of free disk space (Medusa images aren't small) and ~10 minutes
for the first `compose up` while Docker builds both Medusa versions from
source.

---

## Quickstart

```bash
# 1. Clone
git clone https://github.com/boxprobe/scout-medusa
cd scout-medusa

# 2. Bring up Medusa baseline (v2.13.6) + target (v2.14.0)
bash compose/start.sh
# First time: 5-10 minutes per version. Both will be ready when start.sh exits.

# 3. Install scout
pip install boxprobe-scout
playwright install chromium

# 4. Record baseline
scout run scenarios/ --web-version 2.13.6
# This drives the UI through 15 scenarios via Playwright against
# http://localhost:19000/app and records every API call made.

# 5. Record target (point scout at port 29000 this time)
scout run scenarios/ --web-version 2.14.0 \
                     --web-base-url http://localhost:29000/app \
                     --api-base-url http://localhost:29000

# 6. List the two runs to grab their IDs
scout runs

# 7. Diff
scout diff <baseline-run-id> <target-run-id>
```

The diff command opens the HTML report in your browser.

---

## What's inside

### `compose/`

`start.sh` brings up two Medusa instances:

- **Baseline**: `dtc-starter` commit `a57eb51` (Medusa v2.13.6) on
  `http://localhost:19000/app`
- **Target**: `dtc-starter` commit `8327b63` (Medusa v2.14.0) on
  `http://localhost:29000/app`, sharing baseline's Postgres + Redis (saves
  ~5 GB of disk and avoids cross-version DB migration pain)

Both seed `admin@medusa-test.com / supersecret` as the admin user during
first startup.

### `scenarios/`

15 admin scenarios covering: auth (login, logout, redirect-when-logged-out),
api-keys (publishable + secret), campaigns, categories, collections,
customers (including customer-groups), draft-orders, inventory (CRUD +
search), locations, and orders (export). Each scenario is a single
`test.py` declaring pixel-anchored Locators and an async test function.

### `app.json`

Default web/API base URLs (baseline by default), viewport, and the demo
admin credentials. Override with `--web-base-url` / `--api-base-url` on
each `scout run` to point at a different target.

### `diff_ignore.json`

Hand-tuned noise suppression for Medusa: timestamps, IDs, tokens, plus a
few endpoint-specific status-only rules. Without this, the diff report
fills up with `created_at` and ULID noise that drowns out real changes.

---

## Common operations

**Re-run only one scenario**:

```bash
scout run scenarios/auth/login-and-logout --web-version 2.13.6
```

**Open the latest diff report manually**:

```bash
open .scout/diffs/*/report.html
```

**Tear it all down**:

```bash
docker compose -p medusa-target down
docker compose -p medusa-baseline down -v   # -v also wipes the shared DB
docker network rm medusa-shared
```

---

## Pinning a different version pair

Edit `compose/start.sh`:

```bash
BASELINE_COMMIT=<dtc-starter SHA matching your baseline Medusa version>
TARGET_COMMIT=<dtc-starter SHA matching your target Medusa version>
```

Then `bash compose/start.sh` again. Docker will rebuild both images at the
new commits. Most scenarios will still pass if the version delta is small;
larger jumps may require adding new ignore rules to `diff_ignore.json` or
updating Locator bboxes if the admin UI shifts elements.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

The short version: this repo accepts PRs for new scenarios, version-pair
updates, and noise rule additions. It does **not** accept PRs that
substitute CSS selectors or DOM-attribute matching for scout's
pixel-anchored Locators — scout's determinism comes from bbox precision,
and selector-based scenarios would undermine the whole demo.

---

## License

MIT — see [LICENSE](LICENSE).
