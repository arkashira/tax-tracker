import json
from tax_tracker import TaxTracker, ExpenseCategory, ExpenseEntry

def test_add_expense():
    tax_tracker = TaxTracker()
    tax_tracker.add_expense("2022-01-01", 100.0, ExpenseCategory.HOUSING, "Rent")
    assert len(tax_tracker.expense_entries) == 1
    assert tax_tracker.expense_entries[0].date == "2022-01-01"
    assert tax_tracker.expense_entries[0].amount == 100.0
    assert tax_tracker.expense_entries[0].category == ExpenseCategory.HOUSING
    assert tax_tracker.expense_entries[0].description == "Rent"

def test_get_expenses_by_category():
    tax_tracker = TaxTracker()
    tax_tracker.add_expense("2022-01-01", 100.0, ExpenseCategory.HOUSING, "Rent")
    tax_tracker.add_expense("2022-01-02", 50.0, ExpenseCategory.FOOD, "Groceries")
    tax_tracker.add_expense("2022-01-03", 200.0, ExpenseCategory.HOUSING, "Utilities")
    expenses_by_category = tax_tracker.get_expenses_by_category()
    assert len(expenses_by_category) == 2
    assert len(expenses_by_category[ExpenseCategory.HOUSING]) == 2
    assert len(expenses_by_category[ExpenseCategory.FOOD]) == 1

def test_save_to_json():
    tax_tracker = TaxTracker()
    tax_tracker.add_expense("2022-01-01", 100.0, ExpenseCategory.HOUSING, "Rent")
    tax_tracker.save_to_json("expenses.json")
    with open("expenses.json", "r") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["date"] == "2022-01-01"
    assert data[0]["amount"] == 100.0
    assert data[0]["category"] == "housing"
    assert data[0]["description"] == "Rent"

def test_load_from_json():
    tax_tracker = TaxTracker()
    tax_tracker.add_expense("2022-01-01", 100.0, ExpenseCategory.HOUSING, "Rent")
    tax_tracker.save_to_json("expenses.json")
    tax_tracker.load_from_json("expenses.json")
    assert len(tax_tracker.expense_entries) == 1
    assert tax_tracker.expense_entries[0].date == "2022-01-01"
    assert tax_tracker.expense_entries[0].amount == 100.0
    assert tax_tracker.expense_entries[0].category == ExpenseCategory.HOUSING
    assert tax_tracker.expense_entries[0].description == "Rent"
