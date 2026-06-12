from tax_tracker import TaxTracker, Plan

def test_subscribe():
    tax_tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tax_tracker.subscribe(user_id, plan, billing_info)
    assert tax_tracker.get_billing_info(user_id) == billing_info

def test_process_payment():
    tax_tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tax_tracker.subscribe(user_id, plan, billing_info)
    assert tax_tracker.process_payment(user_id)

def test_get_billing_info():
    tax_tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tax_tracker.subscribe(user_id, plan, billing_info)
    assert tax_tracker.get_billing_info(user_id) == billing_info
