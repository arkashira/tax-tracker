# ROADMAP.md – Tax‑Tracker Feedback Module
*Version: 0.1 – Draft (2026‑06‑11)*  

---  

## 📌 Vision  

Provide a **zero‑dependency, standards‑only** feedback collection layer for the Tax‑Tracker SaaS platform that lets freelancers submit structured insights directly from the web UI or CLI, stores them securely on‑premise, and gives product teams fast, query‑able access for continuous improvement.

---  

## 🎯 MVP (Must‑Have for Launch)  

| # | Feature | Description | Acceptance Criteria | MVP‑Critical |
|---|---------|-------------|----------------------|--------------|
| 1 | **CLI Feedback Submission** | `tax-tracker-feedback submit` reads JSON or interactive prompts and writes a record to the local store. | • Works on Python 3.8‑3.12 <br>• Returns `0` on success, non‑zero on validation error <br>• Creates `feedback.json` if missing | ✅ |
| 2 | **JSON‑File Persistence** | All feedback stored in a single `feedback.json` file located in the configurable data directory. | • File is human‑readable, UTF‑8 <br>• Append‑only, never overwrites existing entries <br>• Handles concurrent writes via file‑lock | ✅ |
| 3 | **Schema Validation** | Enforce a strict schema (user_id, timestamp, rating 1‑5, comment, tags). | • Invalid payload returns clear error message <br>• Unit tests cover every field edge case | ✅ |
| 4 | **Retrieval CLI** | `tax-tracker-feedback list [--filter …]` prints a pretty‑table of stored feedback, optionally filtered by date, rating, or tag. | • Supports `--since`, `--until`, `--rating`, `--tag` <br>• Output sortable by column via `--sort` flag | ✅ |
| 5 | **Packaging & Distribution** | Publish as a pure‑Python wheel on internal PyPI; include `setup.cfg` metadata. | • `pip install tax-tracker-feedback` works offline <br>• No external runtime dependencies | ✅ |
| 6 | **Automated Tests & CI** | GitHub Actions run lint, unit tests, and coverage on each PR. | • 90 %+ coverage on core modules <br>• Lint passes `ruff` and `mypy --strict` | ✅ |
| 7 | **Documentation** | README with quick‑start, CLI examples, and schema definition. | • Rendered correctly on GitHub <br>• Includes contribution guide | ✅ |

*All MVP items are **must‑have**; the product cannot be released without them.*

---  

## 🚀 Release 1 – “Feedback Insights”  

**Timeline:** 8 weeks after MVP (Weeks 9‑16)  

| Theme | Feature | Description | Shippable Milestone |
|-------|---------|-------------|---------------------|
| **Export & Integration** | CSV/JSON Export | `tax-tracker-feedback export --format csv|json` for downstream analytics pipelines. | End of Week 12 |
| **Search & Filtering UI** | Simple TUI (text UI) | Interactive curses‑based browser for quick filtering on the terminal. | End of Week 14 |
| **Security Hardening** | Data‑at‑rest encryption | Optional AES‑256 encryption of the JSON store, key supplied via env var. | End of Week 15 |
| **Telemetry** | Submission metrics | Emit anonymized counters (total submissions, success/failure) to a local Prometheus endpoint. | End of Week 16 |
| **Documentation Upgrade** | API reference (Sphinx) | Auto‑generated docs from docstrings, hosted on internal docs site. | End of Week 16 |

---  

## 🌟 Release 2 – “Team Dashboard”  

**Timeline:** 12 weeks after Release 1 (Weeks 17‑28)  

| Theme | Feature | Description | Shippable Milestone |
|-------|---------|-------------|---------------------|
| **Web Front‑end** | Minimal Flask UI | Web page to view, filter, and export feedback; auth via existing Tax‑Tracker SSO token. | End of Week 22 |
| **Bulk Operations** | Tagging & Status | Bulk‑tag feedback (e.g., `needs‑triage`, `feature‑request`) and mark as `resolved`. | End of Week 24 |
| **Analytics** | Sentiment & Trend Charts | Simple sentiment scoring (VADER) and time‑series charts using Plotly‑offline. | End of Week 26 |
| **Role‑Based Access** | Permissions | Read‑only for product managers, write‑only for admins. | End of Week 27 |
| **Scalability** | Pluggable Store Backend | Abstract storage layer; provide a SQLite implementation as an alternative to flat JSON. | End of Week 28 |

---  

## 📅 High‑Level Timeline  

| Week | Milestone |
|------|-----------|
| 1‑2  | Project scaffolding, CI pipeline, initial schema |
| 3‑4  | CLI submit & list commands, file‑lock implementation |
| 5‑6  | Validation, unit tests, documentation draft |
| 7‑8  | MVP release candidate, internal QA, sign‑off |
| 9‑12 | Export formats, TUI, encryption toggle |
| 13‑16| Telemetry, Sphinx docs, MVP → Release 1 freeze |
| 17‑22| Flask UI, auth integration |
| 23‑26| Bulk ops, sentiment analytics |
| 27‑28| RBAC, SQLite backend, Release 2 GA |

---  

## 📌 Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| Concurrency on flat file | Data loss or corruption | Use `portalocker`‑style cross‑platform file lock; add integration test simulating parallel writes. |
| Schema drift as product evolves | Backward incompatibility | Version the schema (`v1`, `v2`) inside the JSON and provide migration script. |
| Security of stored feedback | GDPR / privacy breach | Encryption option (Release 1) + clear data‑retention policy in docs. |
| Adoption barrier for non‑technical freelancers | Low submission volume | Provide both CLI and future web UI; keep CLI commands intuitive and include interactive mode. |
| Dependency creep | Violates “standard‑library‑only” promise | Enforce lint rule that forbids imports outside `stdlib`. |

---  

## 📈 Success Metrics  

| Metric | Target (6 months) |
|--------|-------------------|
| Active freelancers submitting feedback | ≥ 2 % of total user base |
| Average rating response time (CLI) | < 200 ms |
| Export usage (CSV/JSON) | ≥ 30 % of product‑team members |
| Dashboard MAU (Release 2) | ≥ 15 product managers |
| Zero critical bugs in production | 0 |

---  

*Prepared by the Tax‑Tracker Feedback Module team – Senior Product/Engineering Lead*  
*Document version controlled in `docs/ROADMAP.md`*
