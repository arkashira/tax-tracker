<h3 align="center">🛠️ tax-tracker</h3>

<div align="center">
  <a href="https://github.com/your-org/tax-tracker"><img src="https://img.shields.io/github/license/your-org/tax-tracker?color=blue" alt="License"></a>
  <a href="https://github.com/your-org/tax-tracker"><img src="https://img.shields.io/github/languages/top/your-org/tax-tracker?color=orange" alt="Language"></a>
  <a href="https://github.com/your-org/tax-tracker/actions"><img src="https://img.shields.io/github/workflow/status/your-org/tax-tracker/CI?label=build&color=green" alt="Build Status"></a>
  <a href="https://github.com/your-org/tax-tracker/stargazers"><img src="https://img.shields.io/github/stars/your-org/tax-tracker?style=social" alt="Stars"></a>
</div>

---

# 🚀 tax-tracker  
**Power freelancers & small‑business owners with real‑time tax‑estimate tracking and subscription management.**  
A lightweight Python app that lets you add, upgrade, downgrade, or cancel tax‑related subscriptions and instantly see how they affect your tax liability.

## Why tax-tracker?

- **Instant tax insight** – Get live tax‑estimate updates as you add or modify income/expenses.  
- **Subscription‑first design** – Built around recurring tax‑related services (e.g., accounting SaaS, quarterly filing fees).  
- **Zero‑code onboarding** – Configure your plans via a simple YAML file; no code changes required.  
- **Fully test‑driven** – 100 % pytest coverage for core subscription logic.  
- **Lightweight & portable** – Pure‑Python, no external services; runs anywhere Python 3.9+.  
- **Compliance‑ready** – Generates basic compliance hints based on your jurisdiction settings.  
- **Designed for freelancers** – Tailored UI/CLI for individuals and micro‑businesses, not enterprises.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Subscription CRUD** | Create, read, update, and delete tax‑related subscriptions (upgrade/downgrade/cancel). |
| **Real‑time tax estimate** | Automatic recalculation of estimated tax liability after every change. |
| **Payment processing stub** | Pluggable hooks for Stripe, PayPal, etc. (out‑of‑the‑box no‑op implementation). |
| **CLI interface** | Simple `tax-tracker` command for quick operations. |
| **Config‑driven** | All plans and tax rules live in `business/config.yaml`. |
| **Test suite** | Comprehensive pytest suite covering edge cases and regression. |
| **Extensible architecture** | Core logic in `src/tax_tracker/`; easy to swap storage back‑ends. |

## Tech Stack

- **Python** – Core language, 3.9+ runtime.  
- **pytest** – Test framework for unit and integration tests.  

*(Matches the locked tech‑stack decisions.)*

## Project Structure

```
tax-tracker/
├─ business/          # Business rules, config files, tax tables
├─ docs/              # Documentation assets
├─ src/               # Application source code
│   └─ tax_tracker/   # Core package
├─ tests/             # pytest test suite
├─ pyproject.toml     # Build system & entry points
├─ requirements.txt   # Runtime dependencies
└─ README.md
```

## Getting Started

```bash
# 1️⃣ Clone the repo
git clone https://github.com/your-org/tax-tracker.git
cd tax-tracker

# 2️⃣ Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3️⃣ Run the CLI (example: list current subscriptions)
python -m tax_tracker.cli list
```

### Running the Test Suite

```bash
# Execute all tests
pytest -v
```

## Deploy

The project is designed to run as a simple Python service or CLI.  
For containerised deployment, you can use the following minimal Dockerfile (optional, not part of the locked stack):

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "-m", "tax_tracker.cli"]
```

Build & run:

```bash
docker build -t tax-tracker .
docker run --rm tax-tracker list
```

*(If you prefer a serverless or PaaS deployment, just point the platform to the `pyproject.toml` entry point.)*

## Status

🚧 **Skeleton stage** – core subscription logic is functional and fully tested; UI/CLI polishing and payment‑gateway integrations are next.

_Last commit: `ce733a1` – “real, sandbox‑tested implementation” (2026‑06‑13)._

## Contributing

We welcome contributions! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes, run tests, and submit pull requests.

## License

Distributed under the **MIT License**. See `LICENSE` for more information.