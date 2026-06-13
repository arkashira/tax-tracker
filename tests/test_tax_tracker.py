import pytest
from src.tax_tracker import TaxTracker, SubscriptionStatus
from dataclasses import dataclass

@dataclass
class MockSubscription:
    id: str
    status: SubscriptionStatus
    plan: str
    billing_cycle: str

def test_upgrade_subscription():
    tax_tracker = TaxTracker()
    subscription = MockSubscription("1", SubscriptionStatus.ACTIVE, "basic", "monthly")
    tax_tracker.subscriptions["1"] = subscription
    upgraded_subscription = tax_tracker.upgrade_subscription("1", "premium")
    assert upgraded_subscription.plan == "premium"

def test_downgrade_subscription():
    tax_tracker = TaxTracker()
    subscription = MockSubscription("1", SubscriptionStatus.ACTIVE, "premium", "monthly")
    tax_tracker.subscriptions["1"] = subscription
    downgraded_subscription = tax_tracker.downgrade_subscription("1", "basic")
    assert downgraded_subscription.plan == "basic"

def test_cancel_subscription():
    tax_tracker = TaxTracker()
    subscription = MockSubscription("1", SubscriptionStatus.ACTIVE, "basic", "monthly")
    tax_tracker.subscriptions["1"] = subscription
    canceled_subscription = tax_tracker.cancel_subscription("1")
    assert canceled_subscription.status == SubscriptionStatus.CANCELED

def test_process_payment():
    tax_tracker = TaxTracker()
    subscription = MockSubscription("1", SubscriptionStatus.ACTIVE, "basic", "monthly")
    tax_tracker.subscriptions["1"] = subscription
    payment_result = tax_tracker.process_payment("1", 10.99)
    assert payment_result == "Payment processed for 10.99 on subscription 1"

def test_process_payment_subscription_not_found():
    tax_tracker = TaxTracker()
    with pytest.raises(ValueError):
        tax_tracker.process_payment("1", 10.99)
