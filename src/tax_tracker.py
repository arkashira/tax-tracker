from dataclasses import dataclass
from enum import Enum
from typing import Dict

class SubscriptionStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    CANCELED = "canceled"

@dataclass
class Subscription:
    id: str
    status: SubscriptionStatus
    plan: str
    billing_cycle: str

class TaxTracker:
    def __init__(self):
        self.subscriptions: Dict[str, Subscription] = {}

    def upgrade_subscription(self, subscription_id: str, new_plan: str):
        subscription = self.subscriptions.get(subscription_id)
        if subscription:
            subscription.plan = new_plan
            return subscription
        else:
            raise ValueError("Subscription not found")

    def downgrade_subscription(self, subscription_id: str, new_plan: str):
        subscription = self.subscriptions.get(subscription_id)
        if subscription:
            subscription.plan = new_plan
            return subscription
        else:
            raise ValueError("Subscription not found")

    def cancel_subscription(self, subscription_id: str):
        subscription = self.subscriptions.get(subscription_id)
        if subscription:
            subscription.status = SubscriptionStatus.CANCELED
            return subscription
        else:
            raise ValueError("Subscription not found")

    def process_payment(self, subscription_id: str, amount: float):
        subscription = self.subscriptions.get(subscription_id)
        if subscription:
            # Simulate payment processing
            return f"Payment processed for {amount} on subscription {subscription_id}"
        else:
            raise ValueError("Subscription not found")
