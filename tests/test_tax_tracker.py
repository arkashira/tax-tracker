from tax_tracker import TaxTracker, IncomeCategory, IncomeEntry

def test_add_income():
    tracker = TaxTracker()
    tracker.add_income(100.0, IncomeCategory.FREELANCE, "Freelance work")
    assert len(tracker.get_income_entries()) == 1
    assert tracker.get_income_entries()[0].amount == 100.0
    assert tracker.get_income_entries()[0].category == IncomeCategory.FREELANCE
    assert tracker.get_income_entries()[0].description == "Freelance work"

def test_categorize_income():
    tracker = TaxTracker()
    tracker.add_income(100.0, IncomeCategory.FREELANCE, "Freelance work")
    tracker.add_income(200.0, IncomeCategory.SALARY, "Salary")
    categorized_entries = tracker.categorize_income(IncomeCategory.FREELANCE)
    assert len(categorized_entries) == 1
    assert categorized_entries[0].amount == 100.0
    assert categorized_entries[0].category == IncomeCategory.FREELANCE
    assert categorized_entries[0].description == "Freelance work"

def test_save_to_json():
    tracker = TaxTracker()
    tracker.add_income(100.0, IncomeCategory.FREELANCE, "Freelance work")
    tracker.save_to_json("income.json")
    loaded_tracker = TaxTracker.load_from_json("income.json")
    assert len(loaded_tracker.get_income_entries()) == 1
    assert loaded_tracker.get_income_entries()[0].amount == 100.0
    assert loaded_tracker.get_income_entries()[0].category == IncomeCategory.FREELANCE
    assert loaded_tracker.get_income_entries()[0].description == "Freelance work"

def test_load_from_json_file_not_found():
    tracker = TaxTracker.load_from_json("non_existent_file.json")
    assert len(tracker.get_income_entries()) == 0
