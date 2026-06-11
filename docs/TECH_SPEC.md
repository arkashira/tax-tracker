# TECH_SPEC.md – Tax‑Tracker Feedback Module

**Document version:** 1.0  
**Last updated:** 2026‑06‑11  
**Owner:** Product Engineering – Feedback Sub‑Team  
**Repository:** `tax-tracker/feedback`  

---  

## 1. Overview  

The **Tax‑Tracker Feedback Module** is a self‑contained Python package that enables freelancers using the Tax‑Tracker SaaS product to submit structured feedback and allows the product team to retrieve that feedback for analysis.  

* **Goal:** Provide a zero‑dependency, easy‑to‑install component that persists feedback locally in a JSON file while exposing a clean programmatic API and a minimal CLI.  
* **Scope:**  
  * Collect feedback (rating, comments, optional metadata).  
  * Validate input against a strict schema.  
  * Append feedback atomically to a JSON‑Lines store (`feedback.jsonl`).  
  * Retrieve all feedback entries, optionally filtered by date range or rating.  
  * Export data to CSV for downstream analytics.  

---  

## 2. Architecture  

```
+-------------------+        +-------------------+        +-------------------+
|   CLI Entrypoint  |  -->   |   FeedbackService |  -->   |   PersistenceLayer|
+-------------------+        +-------------------+        +-------------------+
        ^                               ^                           ^
        |                               |                           |
        |                               |                           |
        |                               |                           |
        +-------------------+-----------+---------------------------+
                            |
                     +------+------+
                     |   Public API |
                     +------+------+
                            |
                     +------+------+
                     |   Data Model |
                     +-------------+
```

* **CLI Entrypoint** (`tax_tracker_feedback/__main__.py`): parses command‑line arguments, forwards to `FeedbackService`.  
* **Public API** (`tax_tracker_feedback/api.py`): Pythonic functions (`submit_feedback`, `list_feedback`, `export_csv`) used by the CLI and any internal callers.  
* **FeedbackService** (`tax_tracker_feedback/service.py`): business‑logic layer – validation, transformation, error handling.  
* **PersistenceLayer** (`tax_tracker_feedback/store.py`): low‑level I/O – atomic writes to `feedback.jsonl`, reads, and CSV export.  
* **Data Model** (`tax_tracker_feedback/models.py`): Pydantic‑style dataclasses defining the schema.  

All modules are pure‑Python and rely only on the standard library (`json`, `csv`, `datetime`, `pathlib`, `argparse`, `typing`, `dataclasses`).  

---  

## 3. Data Model  

```python
# tax_tracker_feedback/models.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass(frozen=True)
class Feedback:
    """
    Represents a single feedback entry.
    """
    rating: int                     # 1‑5 inclusive
    comment: str                    # free‑form user comment
    submitted_at: datetime = field(default_factory=datetime.utcnow)
    user_id: Optional[str] = None   # optional anonymised identifier
    metadata: Optional[Dict[str, Any]] = None   # any extra key‑value pairs
```

* **Validation rules** (enforced in `FeedbackService.validate`):  
  * `rating` must be integer 1‑5.  
  * `comment` non‑empty, max 2000 characters.  
  * `metadata` keys must be strings; values must be JSON‑serialisable.  

---  

## 4. Public API  

| Function | Signature | Description |
|----------|-----------|-------------|
| `submit_feedback(feedback: Feedback) -> None` | `def submit_feedback(feedback: Feedback) -> None` | Validates and persists a single feedback entry. Raises `FeedbackError` on validation or I/O failure. |
| `list_feedback(start: datetime | None = None, end: datetime | None = None, min_rating: int | None = None) -> List[Feedback]` | `def list_feedback(... ) -> List[Feedback]` | Returns all stored entries, optionally filtered by submission window and/or minimum rating. |
| `export_csv(path: Path) -> None` | `def export_csv(path: Path) -> None` | Writes all feedback to a CSV file with columns: `submitted_at, rating, comment, user_id, metadata_json`. |
| `reset_store() -> None` *(dev only)* | `def reset_store() -> None` | Clears the JSONL file – used in tests. |

All functions raise a custom `FeedbackError` (subclass of `Exception`) with a clear message for callers.

---  

## 5. Persistence Layer  

* **File format:** JSON Lines (`.jsonl`). Each line is a JSON object representing a `Feedback` instance.  
* **Location:** `~/.tax_tracker/feedback.jsonl` (expanded via `Path.home()`). The directory is created on first use.  
* **Atomicity:** Writes use a temporary file (`.tmp`) and `os.replace` to guarantee crash‑safe appends.  
* **Read path:** Lazy line‑by‑line parsing using `json.loads`; memory‑efficient for large stores.  

```python
# tax_tracker_feedback/store.py (excerpt)
def append_feedback(feedback: Feedback) -> None:
    store_path = _store_path()
    tmp_path = store_path.with_suffix('.tmp')
    with tmp_path.open('a', encoding='utf-8') as f:
        json.dump(feedback.__dict__, f)
        f.write('\n')
    os.replace(tmp_path, store_path)
```

---  

## 6. CLI Specification  

```
usage: python -m tax_tracker_feedback [-h] {submit,list,export} ...

Commands:
  submit   Submit a new feedback entry.
  list     Print stored feedback (optional filters).
  export   Export all feedback to a CSV file.
```

* **submit**  
  * `--rating INT` (1‑5, required)  
  * `--comment TEXT` (required)  
  * `--user-id ID` (optional)  
  * `--metadata KEY=VAL` (repeatable)  

* **list**  
  * `--start DATE` (`YYYY-MM-DD`)  
  * `--end DATE`  
  * `--min-rating INT`  

* **export**  
  * `--out PATH` (required)  

All commands output human‑readable status messages and exit with `0` on success, non‑zero on error.

---  

## 7. Tech Stack  

| Layer | Technology | Reason |
|-------|------------|--------|
| Language | Python 3.8+ | Standard library only; matches Tax‑Tracker runtime. |
| Data validation | `dataclasses` + manual checks | No external libs; lightweight. |
| Persistence | File‑system JSONL | No DB required for low‑volume feedback; easy to ship. |
| CLI | `argparse` | Built‑in, sufficient for simple sub‑commands. |
| Testing | `unittest` (std lib) + `tempfile` | No third‑party test frameworks needed. |
| Packaging | `setuptools` (`setup.cfg`) | Standard PyPI‑compatible distribution. |

---  

## 8. Dependencies  

| Package | Version | Scope |
|---------|---------|-------|
| Python standard library | >=3.8 | Runtime & build |
| (none) | – | No external runtime dependencies |

---  

## 9. Deployment & Distribution  

1. **Packaging** – The module is distributed as a wheel (`tax_tracker_feedback‑<version>-py3-none-any.whl`).  
2. **Installation** – `pip install tax_tracker_feedback` (no extra index required).  
3. **Versioning** – Semantic versioning (`MAJOR.MINOR.PATCH`). Current release: `1.0.0`.  
4. **CI/CD** – GitHub Actions workflow (`.github/workflows/ci.yml`) runs:  
   * Lint (`flake8` – optional dev dependency)  
   * Unit tests (`python -m unittest discover -s tests`)  
   * Build wheel and publish to internal PyPI.  

---  

## 10. Security & Privacy  

* **Data at rest** – Stored in plain JSONL under the user’s home directory. No encryption is performed; the module is intended for low‑sensitivity feedback.  
* **PII handling** – `user_id` is optional and should be a pseudonym or hash; the product team must enforce privacy policies upstream.  
* **Input sanitisation** – All fields are JSON‑serialisable; no code execution paths.  

---  

## 11. Error Handling  

| Error Type | Raised By | Typical Cause | Recommended Action |
|------------|-----------|---------------|--------------------|
| `FeedbackError` | API / Service | Validation failure, I/O error | Show user-friendly message; log details. |
| `FileNotFoundError` | Store read | Store file missing (first run) | Treat as empty store; auto‑create on first write. |
| `PermissionError` | Store write | Insufficient FS permissions | Prompt user to adjust directory permissions. |

All errors are logged to `stderr` with a timestamp (via `logging` module configured in `__init__.py`).

---  

## 12. Testing Strategy  

* **Unit tests** (`tests/`): cover validation, persistence (append/read), CLI parsing, and CSV export.  
* **Property‑based sanity** – generate random valid/invalid `Feedback` objects and assert correct error handling.  
* **Integration test** – spin up a temporary home directory (`HOME` env var) and run the full CLI flow (`submit` → `list` → `export`).  

Test coverage target: **≥ 90%** of module lines.

---  

## 13. Future Enhancements (post‑validation)  

| Feature | Rationale | Estimated Effort |
|---------|-----------|------------------|
| Remote backend (REST API) | Centralised analytics across all freelancers | 2‑3 sprints |
| Encryption at rest | Compliance for sensitive feedback | 1 sprint |
| Rate‑limiting / deduplication | Prevent spam submissions | 1 sprint |
| UI widget (React) | Inline feedback in web app | Separate front‑end repo |

---  

## 14. Glossary  

* **Feedback** – Structured user input consisting of a rating, comment, and optional metadata.  
* **JSONL** – JSON Lines; each line is a complete JSON document.  
* **CLI** – Command‑Line Interface.  

---  

*Prepared by the Tax‑Tracker Feedback Engineering Team.*
