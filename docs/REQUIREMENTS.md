# Requirements Document  
**Project:** tax‑tracker – Feedback Module  
**Author:** Senior Product/Engineering Lead  
**Date:** 2026‑06‑11  

---  

## 1. Overview  

The Feedback Module is a lightweight, standard‑library‑only Python component that enables freelancers using the Tax‑Tracker product to submit structured feedback and allows the product team to retrieve that feedback for analysis. All data is persisted locally in a JSON file; no external services or third‑party packages are required.  

The module must be production‑ready, secure, and performant while remaining simple to install (Python 3.8+).  

---  

## 2. Functional Requirements  

| ID | Description |
|----|-------------|
| **FR‑1** | **Submit Feedback** – Provide a public function `submit_feedback(user_id: str, rating: int, comment: str, tags: List[str] = None) -> None` that validates input, appends a new feedback entry to the JSON store, and returns nothing. |
| **FR‑2** | **Feedback Schema** – Each feedback entry must contain the fields: `id` (UUID v4), `timestamp` (ISO‑8601 UTC), `user_id`, `rating` (1‑5 integer), `comment` (max 500 chars), `tags` (optional list of non‑empty strings), and `version` (module version). |
| **FR‑3** | **Persistence** – Store feedback in a configurable file path (default `./feedback.json`). The file must be created on first write if it does not exist and must be human‑readable JSON with one top‑level array of entries. |
| **FR‑4** | **Retrieve All Feedback** – Provide a function `get_all_feedback() -> List[Dict]` that returns a deep copy of all stored entries, sorted by `timestamp` descending. |
| **FR‑5** | **Query API** – Provide a function `query_feedback(rating: Optional[int] = None, tags: Optional[Set[str]] = None, start: Optional[datetime] = None, end: Optional[datetime] = None) -> List[Dict]` that filters entries based on the supplied criteria (any combination). |
| **FR‑6** | **CLI Interface** – Expose a command‑line entry point `tax_tracker_feedback` with sub‑commands: `submit` (prompts for fields or accepts `--json` payload) and `list` (pretty‑prints all entries, supports `--rating`, `--tag`, `--since`, `--until`). |
| **FR‑7** | **Export** – Provide `export_feedback(path: str, format: Literal["json","csv"]) -> None` to write the current dataset to the given location in the requested format. |
| **FR‑8** | **Import** – Provide `import_feedback(path: str, format: Literal["json","csv"], merge: bool = True) -> None` that reads external data, validates each entry against the schema, and either merges with or replaces the existing store. |
| **FR‑9** | **Audit Log** – Every successful `submit`, `import`, or `export` operation must append a line to a separate audit log file (`feedback_audit.log`) containing timestamp, operation, user_id (if applicable), and outcome (success/failure). |
| **FR‑10** | **Graceful Degradation** – If the JSON store becomes corrupted, the module must raise a custom `FeedbackStoreError` with a clear message and must not overwrite the corrupted file. |
| **FR‑11** | **Unit Test Coverage** – Provide a test suite (`tests/`) with ≥ 90 % line coverage, exercising all public APIs, error paths, and CLI commands. |
| **FR‑12** | **Documentation** – Auto‑generate API docs via `pydoc` and include a `README.md` usage section covering both library and CLI usage. |

---  

## 3. Non‑Functional Requirements  

| ID | Requirement |
|----|-------------|
| **NFR‑1** | **Performance** – Adding a feedback entry must complete in ≤ 5 ms for a store size up to 100 k entries on typical developer hardware (Intel i5, 8 GB RAM). Retrieval of all entries must complete in ≤ 20 ms for the same size. |
| **NFR‑2** | **Scalability** – The JSON store must support up to 1 million entries without exceeding 2 GB of disk space; operations must degrade gracefully (see NFR‑1). |
| **NFR‑3** | **Security** – All file I/O must use the `os` and `json` modules with explicit mode flags to prevent race conditions. The module must reject any input containing control characters (`\0`, `\x1b`, etc.) in `comment` or `tags`. |
| **NFR‑4** | **Data Integrity** – Writes must be atomic: write to a temporary file and rename on success. Use file locking (`fcntl` on POSIX, `msvcrt` on Windows) to prevent concurrent corruption. |
| **NFR‑5** | **Reliability** – The module must survive unexpected termination during a write; on next load it must detect incomplete temp files and either recover or raise `FeedbackStoreError`. |
| **NFR‑6** | **Portability** – Must run on Windows, macOS, and Linux without modification. No external dependencies beyond the Python standard library. |
| **NFR‑7** | **Maintainability** – Code style must follow PEP 8, include type hints (PEP 484), and be linted with `flake8` (max line length 88). |
| **NFR‑8** | **Observability** – The audit log must be rotated daily, keeping the last 30 days (`feedback_audit.log.YYYY-MM-DD`). |
| **NFR‑9** | **Compliance** – All stored data must be treated as personal data; the module must provide a `purge_user(user_id: str) -> int` function that deletes all entries for a given user and returns the number of removed records. |
| **NFR‑10** | **Versioning** – The module must expose `__version__` following Semantic Versioning 2.0.0. The `version` field in each entry must match this value at submission time. |

---  

## 4. Constraints  

1. **Standard‑Library Only** – No third‑party packages may be added; all functionality must be built on the Python 3.8+ stdlib.  
2. **File Location Configurable** – The JSON store path and audit log directory must be overridable via environment variables `FEEDBACK_STORE_PATH` and `FEEDBACK_AUDIT_DIR`.  
3. **No Network Calls** – The module must not perform any outbound network communication.  
4. **Backward Compatibility** – Existing feedback files created by version 0.1.x must be readable; unknown fields should be ignored but preserved on export.  

---  

## 5. Assumptions  

| ID | Assumption |
|----|------------|
| **A‑1** | The target deployment environment has write permission to the directory containing the JSON store and audit log. |
| **A‑2** | Concurrent access will be limited to a small number of processes (≤ 5) on the same host; distributed concurrency is out of scope. |
| **A‑3** | Users are freelancers identified by a stable UUID string supplied by the surrounding Tax‑Tracker application. |
| **A‑4** | The maximum comment length (500 chars) is sufficient for all intended feedback use‑cases. |
| **A‑5** | The product team will handle downstream analysis; the module only needs to provide raw data export. |
| **A‑6** | Timezone handling is UTC‑only; any local‑time conversion is performed by consumers. |

---  

## 6. Acceptance Criteria  

1. All functional requirements FR‑1 – FR‑12 are implemented and pass the provided unit tests.  
2. Performance benchmarks meet NFR‑1 on the reference hardware.  
3. Security and data‑integrity tests (simulated concurrent writes, corrupted file injection) succeed without data loss.  
4. Documentation and CLI usage examples are complete and verified by a non‑developer stakeholder.  
5. The module can be installed via `pip install .` (editable mode) and the CLI `tax_tracker_feedback` is discoverable in `$PATH`.  

---  

*End of Requirements Document*
