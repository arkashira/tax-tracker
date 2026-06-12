import json
import os
from dataclasses import asdict, dataclass, field
from typing import List, Optional


@dataclass
class Expense:
    """A single expense entry."""
    date: str               # ISO format e.g. "2023-04-01"
    amount: float
    category: str
    description: str = ""

    def to_dict(self) -> dict:
        """Convert the expense to a JSON‑serialisable dict."""
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Expense":
        """Create an Expense from a dict (as produced by `to_dict`)."""
        return Expense(
            date=data["date"],
            amount=data["amount"],
            category=data["category"],
            description=data.get("description", ""),
        )


class ExpenseTracker:
    """
    Simple in‑memory expense tracker with optional JSON persistence.
    """

    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialise the tracker.

        Args:
            storage_path: Path to a JSON file for persisting data.
                          If ``None`` the tracker works purely in memory.
        """
        self._expenses: List[Expense] = []
        self._storage_path = storage_path
        if storage_path:
            self._load()

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def add_expense(
        self,
        date: str,
        amount: float,
        category: str,
        description: str = "",
    ) -> None:
        """
        Add a new expense entry.

        Args:
            date: Date string (ISO format recommended).
            amount: Monetary amount (positive float).
            category: Category name (e.g. "Travel").
            description: Optional free‑form description.
        """
        expense = Expense(date=date, amount=amount, category=category, description=description)
        self._expenses.append(expense)
        self._save()

    def list_expenses(self) -> List[Expense]:
        """Return a copy of all stored expenses."""
        return list(self._expenses)

    def get_by_category(self, category: str) -> List[Expense]:
        """Return expenses that match the given category."""
        return [e for e in self._expenses if e.category == category]

    # ------------------------------------------------------------------ #
    # Persistence helpers
    # ------------------------------------------------------------------ #
    def _save(self) -> None:
        """Write the current expense list to the JSON file, if persistence is enabled."""
        if not self._storage_path:
            return
        data = [e.to_dict() for e in self._expenses]
        try:
            with open(self._storage_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        except OSError as exc:
            # In a tiny utility we simply surface the error; callers can handle it.
            raise RuntimeError(f"Failed to save expenses to {self._storage_path}") from exc

    def _load(self) -> None:
        """Load expenses from the JSON file, if it exists."""
        if not os.path.exists(self._storage_path):
            # No file yet – start with an empty list.
            self._expenses = []
            return
        try:
            with open(self._storage_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
            self._expenses = [Expense.from_dict(item) for item in raw]
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"Failed to load expenses from {self._storage_path}") from exc
