import json
from dataclasses import dataclass
from enum import Enum
from typing import List

class IncomeCategory(Enum):
    FREELANCE = "freelance"
    SALARY = "salary"
    INVESTMENTS = "investments"

@dataclass
class IncomeEntry:
    amount: float
    category: IncomeCategory
    description: str

class TaxTracker:
    def __init__(self):
        self.income_entries = []

    def add_income(self, amount: float, category: IncomeCategory, description: str):
        income_entry = IncomeEntry(amount, category, description)
        self.income_entries.append(income_entry)

    def get_income_entries(self):
        return self.income_entries

    def categorize_income(self, category: IncomeCategory):
        return [entry for entry in self.income_entries if entry.category == category]

    def save_to_json(self, filename: str):
        data = [{"amount": entry.amount, "category": entry.category.value, "description": entry.description} for entry in self.income_entries]
        with open(filename, "w") as f:
            json.dump(data, f)

    @classmethod
    def load_from_json(cls, filename: str):
        tracker = cls()
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for entry_data in data:
                    category = IncomeCategory(entry_data["category"])
                    income_entry = IncomeEntry(entry_data["amount"], category, entry_data["description"])
                    tracker.income_entries.append(income_entry)
        except FileNotFoundError:
            pass
        return tracker
