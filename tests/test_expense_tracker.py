import os
import tempfile

import pytest

from expense_tracker import Expense, ExpenseTracker


def test_add_and_list_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense("2023-01-01", 100.0, "Office Supplies", "Printer paper")
    tracker.add_expense("2023-01-15", 250.5, "Travel", "Flight to client")

    expenses = tracker.list_expenses()
    assert len(expenses) == 2

    # Verify first expense fields
    first = expenses[0]
    assert first.date == "2023-01-01"
    assert first.amount == 100.0
    assert first.category == "Office Supplies"
    assert first.description == "Printer paper"

    # Verify second expense fields
    second = expenses[1]
    assert second.date == "2023-01-15"
    assert second.amount == 250.5
    assert second.category == "Travel"
    assert second.description == "Flight to client"


def test_category_filtering():
    tracker = ExpenseTracker()
    tracker.add_expense("2023-02-01", 75.0, "Travel", "Taxi")
    tracker.add_expense("2023-02-02", 30.0, "Meals", "Lunch")
    tracker.add_expense("2023-02-03", 120.0, "Travel", "Train ticket")

    travel = tracker.get_by_category("Travel")
    meals = tracker.get_by_category("Meals")
    other = tracker.get_by_category("Software")

    assert len(travel) == 2
    assert all(e.category == "Travel" for e in travel)

    assert len(meals) == 1
    assert meals[0].category == "Meals"

    assert len(other) == 0


def test_persistence_to_file():
    # Use a temporary file to avoid side effects.
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "expenses.json")
        tracker = ExpenseTracker(storage_path=path)

        tracker.add_expense("2023-03-01", 55.0, "Software", "Subscription")
        tracker.add_expense("2023-03-05", 200.0, "Equipment", "Monitor")

        # Create a new tracker pointing at the same file – it should load the data.
        new_tracker = ExpenseTracker(storage_path=path)
        loaded = new_tracker.list_expenses()
        assert len(loaded) == 2
        categories = {e.category for e in loaded}
        assert categories == {"Software", "Equipment"}
