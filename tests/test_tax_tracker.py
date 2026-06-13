from tax_tracker import TaxTracker, Plan

def test_subscribe():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    assert tracker.get_billing_info(user_id) == billing_info

def test_process_payment():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    assert tracker.process_payment(user_id) == True

def test_get_billing_info():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    assert tracker.get_billing_info(user_id) == billing_info
