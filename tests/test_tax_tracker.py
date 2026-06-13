from tax_tracker import TaxTracker, Plan, Subscription
import pytest

def test_subscribe():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    assert tracker.get_subscription(user_id).plan == plan
    assert tracker.get_subscription(user_id).billing_info == billing_info

def test_subscribe_duplicate():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    with pytest.raises(ValueError):
        tracker.subscribe(user_id, plan, billing_info)

def test_get_subscription():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    subscription = tracker.get_subscription(user_id)
    assert subscription.plan == plan
    assert subscription.billing_info == billing_info

def test_process_payment():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    amount = 10.99
    result = tracker.process_payment(user_id, amount)
    assert result == f"Payment processed for {user_id}: {amount}"

def test_get_billing_info():
    tracker = TaxTracker()
    user_id = "user1"
    plan = Plan.COMPREHENSIVE
    billing_info = {"name": "John Doe", "card_number": "1234-5678-9012-3456"}
    tracker.subscribe(user_id, plan, billing_info)
    result = tracker.get_billing_info(user_id)
    assert result == billing_info
