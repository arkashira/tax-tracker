import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict

class Plan(Enum):
    BASIC = 1
    COMPREHENSIVE = 2

@dataclass
class Subscription:
    plan: Plan
    billing_info: Dict[str, str]

class TaxTracker:
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, user_id: str, plan: Plan, billing_info: Dict[str, str]):
        self.subscriptions[user_id] = Subscription(plan, billing_info)

    def process_payment(self, user_id: str):
        subscription = self.subscriptions.get(user_id)
        if subscription:
            # Process payment securely (mock implementation)
            print(f"Processing payment for {user_id}...")
            return True
        return False

    def get_billing_info(self, user_id: str):
        subscription = self.subscriptions.get(user_id)
        if subscription:
            return subscription.billing_info
        return None
