<h3 align="center">🛠️ tax-tracker</h3>

<div align="center">
  <a href="https://github.com/your-org/tax-tracker/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://github.com/your-org/tax-tracker"><img src="https://img.shields.io/github/languages/top/your-org/tax-tracker?color=blue" alt="Language"></a>
  <a href="https://github.com/your-org/tax-tracker/actions"><img src="https://img.shields.io/github/workflow/status/your-org/tax-tracker/CI?label=build" alt="Build Status"></a>
  <a href="https://github.com/your-org/tax-tracker/stargazers"><img src="https://img.shields.io/github/stars/your-org/tax-tracker?style=social" alt="Stars"></a>
</div>

---

# 🚀 tax-tracker
**Power freelancers & small‑business owners with effortless tax tracking.** A comprehensive tax‑management tool that automates expense/income logging, estimates taxes in real‑time, and presents a clean UI that anyone can use—no accounting degree required.

## Why tax-tracker?
- **Zero‑Math Hassle** – Auto‑calculates quarterly tax estimates, cutting missed‑payment risk by >30 %.
- **All‑in‑One Dashboard** – Consolidates expenses, income, and deductions in a single view.
- **Non‑Accountant Friendly** – Guided data entry and plain‑language reports keep the learning curve under 5 minutes.
- **Compliance‑First** – Built around IRS/Thai‑Revenue guidelines to keep you audit‑ready.
- **Secure & Private** – All data stored locally or encrypted in the cloud; no third‑party scraping.
- **Extensible** – Plug‑in architecture lets you add custom categories or integrate with bookkeeping SaaS.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Expense & Income Capture** | Quick entry forms, CSV import, and bank‑feed connectors. |
| **Real‑Time Tax Estimation** | Calculates federal, state, and local liabilities as you log data. |
| **What‑If Scenarios** | Simulate deductions, filing status changes, and forecast year‑end tax. |
| **Report Generation** | Export PDF/Excel summaries ready for filing or accountant review. |
| **Multi‑Currency Support** | Automatic FX conversion using daily rates. |
| **Data Export & Backup** | One‑click backup to encrypted ZIP or cloud bucket. |
| **API / CLI** | Programmatic access for automation scripts or CI pipelines. |

## Tech Stack
> The definitive stack is documented in `decisions/tech-stack.md`.  
> **Please refer to that file for the exact versions and choices.**  

## Project Structure
```
tax-tracker/
├─ business/          # Domain‑logic (services, models, tax rules)
├─ docs/              # Documentation, design docs, API specs
├─ src/               # Application source code
│   ├─ __main__.py    # Entry point for CLI
│   └─ ...            # Packages & modules
├─ tests/             # Unit & integration test suite
├─ README.md
├─ pyproject.toml     # Build config, entry points, dependencies
└─ requirements.txt   # Pin‑exact pip requirements
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/your-org/tax-tracker.git
cd tax-tracker

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application (CLI entry point defined in pyproject.toml)
python -m src          # or `tax-tracker` if installed as a console script
```

### Running the Test Suite
```bash
# From the repository root
pytest tests
```

## Deploy

> Deployment instructions depend on the stack defined in `decisions/tech-stack.md`.  
> Typical options include Docker, AWS Lambda, or a simple systemd service.  
> Please consult the tech‑stack doc for the exact commands.

## Status
🟢 Actively maintained – latest commit `5457a87` (2026‑06‑10) adds final CI pipeline and version bump.

## Contributing
We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
This project is licensed under the **MIT License**.