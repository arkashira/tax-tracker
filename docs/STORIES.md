# STORIES.md – Tax‑Tracker Feedback Module

## Overview
The **Tax‑Tracker Feedback Module** is a lightweight, standard‑library‑only Python component that enables freelancers using the Tax‑Tracker product to submit structured feedback and allows the product team to retrieve that feedback for analysis.  
The following backlog is organized into **Epics** that map to the core capabilities of the module. Stories are ordered to deliver a Minimum Viable Product (MVP) first, then incremental enhancements.

---

## EPIC 1 – Core Feedback Capture & Persistence  

*Goal: Provide a reliable, zero‑dependency way for users to submit feedback that is safely persisted locally.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 1 | **As a freelancer, I want to submit feedback via the CLI, so that I can share my experience without leaving the terminal.** | - `tax_tracker_feedback submit` command launches an interactive prompt.<br>- Prompts collect: `rating (1‑5)`, `category (e.g., UI, performance, feature request)`, `title`, `description`.<br>- All fields are required except `description` (optional).<br>- On successful submission, the CLI prints a confirmation message with a generated `feedback_id`. |
| 2 | **As a freelancer, I want my feedback to be stored locally in a JSON file, so that it is not lost between sessions.** | - Feedback is appended to `feedback.json` in the module’s data directory (`~/.tax_tracker/feedback.json`).<br>- The JSON file contains an array of feedback objects, each with keys: `id`, `timestamp`, `rating`, `category`, `title`, `description`, `user_agent`.<br>- File is created automatically on first submission if it does not exist. |
| 3 | **As a developer, I want the module to validate input before persisting, so that the data quality is guaranteed.** | - Rating must be an integer 1‑5; invalid input re‑prompts the user.<br>- Category must be one of the predefined list; unknown values are rejected with a helpful error.<br>- Title must be non‑empty and ≤ 120 characters.<br>- Description, if provided, ≤ 1000 characters.<br>- Validation errors are displayed clearly and do not write to the file. |
| 4 | **As a freelancer, I want to see a summary of my submitted feedback, so that I can verify what was recorded.** | - After submission, the CLI prints a formatted summary (ID, timestamp, rating, category, title).<br>- The summary matches the data stored in `feedback.json`. |

---

## EPIC 2 – Retrieval & Export for Product Team  

*Goal: Enable the product team to access, filter, and export collected feedback.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 5 | **As a product analyst, I want to list all feedback entries, so that I can review what users have submitted.** | - `tax_tracker_feedback list` prints a table of all entries with columns: `ID`, `Date`, `Rating`, `Category`, `Title`.<br>- Output is sorted by newest first.<br>- If no feedback exists, a friendly “No feedback found” message is shown. |
| 6 | **As a product analyst, I want to filter feedback by rating or category, so that I can focus on specific issues.** | - `tax_tracker_feedback list --rating 1` shows only entries with rating = 1.<br>- `tax_tracker_feedback list --category UI` shows only UI‑related entries.<br>- Multiple filters can be combined (e.g., rating = 1 **and** category = UI). |
| 7 | **As a product analyst, I want to export feedback to a CSV file, so that I can import it into BI tools.** | - `tax_tracker_feedback export --output feedback.csv` creates a CSV with headers matching the JSON keys (except `user_agent`).<br>- Export respects any active filters (`--rating`, `--category`).<br>- File is written to the current working directory; existing files are overwritten after user confirmation. |
| 8 | **As a product analyst, I want a programmatic API to fetch feedback, so that I can integrate it into internal dashboards.** | - The module exposes a function `load_feedback(filter: dict = None) -> List[dict]`.<br>- Function returns a list of feedback dicts matching the optional filter (same keys as CLI filters).<br>- Raises a custom `FeedbackError` with a clear message on file‑access problems. |

---

## EPIC 3 – Robustness & Operational Concerns  

*Goal: Ensure the module behaves predictably in production environments.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 9 | **As a system administrator, I want the module to handle a corrupted JSON file gracefully, so that the application does not crash.** | - On load, if `feedback.json` is invalid JSON, the module backs up the corrupted file (`feedback.json.bak.<timestamp>`).<br>- A new empty `feedback.json` is created and the user is notified of the recovery action. |
| 10 | **As a developer, I want unit tests covering all core functions, so that future changes do not break existing behavior.** | - Tests exist for submission, validation, persistence, listing, filtering, and export.<br>- Test suite runs with `python -m unittest discover` and achieves ≥ 90 % coverage. |
| 11 | **As a freelancer, I want the CLI to have a `--help` flag, so that I can discover commands without reading docs.** | - `tax_tracker_feedback --help` displays usage, sub‑commands, and options.<br>- Each sub‑command (`submit`, `list`, `export`) also supports `--help`. |
| 12 | **As a product manager, I want the feedback file location to be configurable via an environment variable, so that we can store data in a shared location on CI/CD runners.** | - If `TAX_TRACKER_FEEDBACK_PATH` is set, the module reads/writes to that path instead of the default `~/.tax_tracker/feedback.json`.<br>- Invalid paths produce a clear error and fallback to the default with a warning. |
| 13 | **As a security‑concerned stakeholder, I want the stored feedback to be readable only by the owning user, so that sensitive comments are protected.** | - On creation, the feedback file is set to mode `0o600` (owner read/write only) on POSIX systems.<br>- On Windows, the file is created with default ACLs and a warning is logged that strict permissions are not enforced. |

---

## EPIC 4 – Future Enhancements (Post‑MVP)  

*Goal: Outline longer‑term ideas that are out of scope for the initial release but valuable for roadmap planning.*

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| 14 | **As a freelancer, I want to attach a screenshot to my feedback, so that I can illustrate UI bugs.** | - CLI accepts an optional `--attachment <path>` argument.<br>- Attachments are copied to a sub‑folder `attachments/` and referenced in the JSON entry. |
| 15 | **As a product analyst, I want sentiment analysis tags (positive/negative/neutral) automatically added, so that I can prioritize pain points.** | - After submission, the module runs a lightweight sentiment heuristic on `title` + `description` and stores a `sentiment` field.<br>- No external libraries are used; simple keyword‑based scoring is sufficient for MVP. |
| 16 | **As a DevOps engineer, I want the module to support remote storage back‑ends (e.g., S3, Google Cloud Storage), so that feedback can be aggregated across machines.** | - Abstract storage layer with a `StorageInterface` allowing plug‑ins.<br>- Provide a stub implementation for local JSON and a documented interface for future cloud adapters. |

---

## Prioritization & MVP Scope
- **MVP** includes Epics 1, 2 (stories 1‑8) and essential robustness from Epic 3 (stories 9‑12).  
- Stories 13‑16 are **post‑MVP** items slated for later sprints.

--- 

*Prepared by: Senior Product/Engineering Lead*  
*Date: 2026‑06‑11*
