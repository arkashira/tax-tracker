<h3 align="center">🛠️ tax-tracker</h3>

<div align="center">
  <a href="https://github.com/your-org/tax-tracker"><img src="https://img.shields.io/github/stars/your-org/tax-tracker?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/your-org/tax-tracker/blob/main/LICENSE"><img src="https://img.shields.io/github/license/your-org/tax-tracker?style=flat-square" alt="License"></a>
  <a href="https://github.com/your-org/tax-tracker"><img src="https://img.shields.io/badge/language-Python%203.11-blue?style=flat-square" alt="Language"></a>
  <a href="https://github.com/your-org/tax-tracker/actions"><img src="https://img.shields.io/github/workflow/status/your-org/tax-tracker/CI?label=build&style=flat-square" alt="Build"></a>
</div>

---

# 🚀 tax-tracker
**Power everyday users with effortless tax‑tracking and automatic tax‑estimation.** A comprehensive, user‑friendly tool that turns messy finances into clear, compliant tax reports—no accounting degree required.

## Why tax-tracker?
- **Zero‑Math Needed** – All calculations are done for you; just input expenses/income.
- **Stay Penalty‑Free** – Real‑time tax‑estimation warns you before under‑payment deadlines.
- **All‑In‑One Dashboard** – View income, deductions, and projected tax liability at a glance.
- **Non‑Accountant Friendly** – Plain‑language UI + guided wizards reduce learning curve.
- **Secure & Private** – Data stored locally or in encrypted cloud storage of your choice.
- **Extensible** – Plug‑in support for additional tax jurisdictions and reporting formats.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Expense & Income Capture** | Quick entry forms, CSV import, and bank‑statement parsing. |
| **Automated Tax Estimation** | Calculates provisional tax based on current rules for your jurisdiction. |
| **What‑If Scenarios** | Simulate changes (e.g., new deduction) and see tax impact instantly. |
| **Reporting** | Generate PDF/Excel tax reports ready for filing or accountant review. |
| **Multi‑Year Support** | Store and compare data across fiscal years. |
| **Data Export/Import** | Backup to JSON or restore from previous exports. |
| **Localization** | UI available in English and Thai (future languages planned). |

## Tech Stack
*The definitive tech‑stack will be recorded in `decisions/tech-stack.md` once locked.*  
Current repository structure indicates a **Python** project managed via **pyproject.toml** (likely Poetry or setuptools). No additional technologies are assumed beyond what the lock later defines.

## Project Structure
```
tax-tracker/
├─ business/          # Domain‑specific business logic (tax rules, calculations)
├─ src/               # Core application code (CLI, UI, data models)
├─ tests/             # Unit and integration test suite
├─ README.md
└─ pyproject.toml     # Build system, dependencies, entry points
```

## Getting Started

> **Prerequisite** – Python 3.11+ installed and `pip` available.

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-org/tax-tracker.git
cd tax-tracker

# 2️⃣ Install the package (editable mode)
pip install -e .

# 3️⃣ Run the CLI (entry point defined in pyproject.toml)
tax-tracker --help
```

### Running the Test Suite
```bash
# Using the built‑in test runner (pytest assumed)
pytest -q
```

## Deploy
Deployment instructions will be added once the deployment target is locked in `decisions/tech-stack.md`. Typical options may include:

- **Docker** container for self‑hosting  
- **Serverless** (AWS Lambda / Cloudflare Workers) for API‑only usage  

Stay tuned for the final deployment guide.

## Status
🚧 **In active development** – latest commit `8ce1a11` (2026‑06‑10) adds the CI build pipeline.

## Contributing
We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes, run tests, and submit pull requests.

## License
This project is licensed under the **MIT License**.