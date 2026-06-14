import json
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class ExpenseCategory(Enum):
    HOUSING = "housing"
    TRANSPORTATION = "transportation"
    FOOD = "food"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"

@dataclass
class ExpenseEntry:
    date: str
    amount: float
    category: ExpenseCategory
    description: str

class TaxTracker:
    def __init__(self):
        self.expense_entries = []

    def add_expense(self, date: str, amount: float, category: ExpenseCategory, description: str):
        expense_entry = ExpenseEntry(date, amount, category, description)
        self.expense_entries.append(expense_entry)

    def get_expenses_by_category(self) -> Dict[ExpenseCategory, List[ExpenseEntry]]:
        expenses_by_category = {}
        for expense_entry in self.expense_entries:
            if expense_entry.category not in expenses_by_category:
                expenses_by_category[expense_entry.category] = []
            expenses_by_category[expense_entry.category].append(expense_entry)
        return expenses_by_category

    def save_to_json(self, filename: str):
        data = []
        for expense_entry in self.expense_entries:
            data.append({
                "date": expense_entry.date,
                "amount": expense_entry.amount,
                "category": expense_entry.category.value,
                "description": expense_entry.description
            })
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_json(self, filename: str):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.expense_entries = []
            for expense_data in data:
                expense_entry = ExpenseEntry(
                    date=expense_data["date"],
                    amount=expense_data["amount"],
                    category=ExpenseCategory(expense_data["category"]),
                    description=expense_data["description"]
                )
                self.expense_entries.append(expense_entry)
        except FileNotFoundError:
            pass
