import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict

class Plan(Enum):
    BASIC = "basic"
    COMPREHENSIVE = "comprehensive"

@dataclass
class Subscription:
    plan: Plan
    billing_info: Dict[str, str]

class TaxTracker:
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, user_id: str, plan: Plan, billing_info: Dict[str, str]):
        if user_id in self.subscriptions:
            raise ValueError("User already subscribed")
        self.subscriptions[user_id] = Subscription(plan, billing_info)

    def get_subscription(self, user_id: str):
        return self.subscriptions.get(user_id)

    def process_payment(self, user_id: str, amount: float):
        subscription = self.get_subscription(user_id)
        if subscription is None:
            raise ValueError("User not subscribed")
        # Process payment securely (in-memory stand-in)
        return f"Payment processed for {user_id}: {amount}"

    def get_billing_info(self, user_id: str):
        subscription = self.get_subscription(user_id)
        if subscription is None:
            raise ValueError("User not subscribed")
        return subscription.billing_info
