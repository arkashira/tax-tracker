import json
import uuid
from datetime import datetime
from dataclasses import dataclass, asdict
from pathlib import Path
import argparse
import sys

@dataclass
class FeedbackEntry:
    """Represents a single piece of user feedback."""
    id: str
    user_id: str
    message: str
    timestamp: str

class FeedbackSystem:
    """
    Manages the collection, storage, and retrieval of user feedback.
    Uses a JSON file for persistence.
    """
    def __init__(self, storage_path: str = "feedback_data.json"):
        self.storage_path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Creates the storage file if it does not exist."""
        if not self.storage_path.exists():
            self.storage_path.write_text("[]", encoding="utf-8")

    def _load_data(self) -> list:
        """Reads feedback data from the JSON file."""
        try:
            content = self.storage_path.read_text(encoding="utf-8")
            return json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_data(self, data: list):
        """Writes feedback data to the JSON file."""
        self.storage_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def submit_feedback(self, user_id: str, message: str) -> FeedbackEntry:
        """
        Acceptance Criteria: User can submit feedback.
        Acceptance Criteria: Feedback is collected and stored.
        """
        entry = FeedbackEntry(
            id=str(uuid.uuid4()),
            user_id=user_id,
            message=message,
            timestamp=datetime.now().isoformat()
        )
        
        current_data = self._load_data()
        current_data.append(asdict(entry))
        self._save_data(current_data)
        
        return entry

    def get_all_feedback(self) -> list[FeedbackEntry]:
        """
        Acceptance Criteria: Feedback is accessible to the product team.
        """
        data = self._load_data()
        return [FeedbackEntry(**item) for item in data]

def main():
    """CLI interface for the feedback system."""
    parser = argparse.ArgumentParser(description="Tax-Tracker Feedback System")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Submit command
    submit_parser = subparsers.add_parser("submit", help="Submit new feedback")
    submit_parser.add_argument("--user", required=True, help="ID of the user submitting feedback")
    submit_parser.add_argument("--message", required=True, help="The feedback message")

    # List command
    list_parser = subparsers.add_parser("list", help="List all collected feedback")

    args = parser.parse_args()
    system = FeedbackSystem()

    if args.command == "submit":
        entry = system.submit_feedback(args.user, args.message)
        print(f"Success! Feedback ID: {entry.id}")
    elif args.command == "list":
        feedbacks = system.get_all_feedback()
        if not feedbacks:
            print("No feedback found.")
        else:
            print(f"Total Feedback Entries: {len(feedbacks)}\n")
            for f in feedbacks:
                print(f"[{f.timestamp}] ID: {f.id} | User: {f.user_id}")
                print(f"Message: {f.message}\n")

if __name__ == "__main__":
    main()
