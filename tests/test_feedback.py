import pytest
import json
from pathlib import Path
from feedback import FeedbackSystem

def test_user_can_submit_feedback(tmp_path):
    """
    Acceptance Criteria: User can submit feedback.
    Acceptance Criteria: Feedback is collected and stored.
    """
    # Arrange
    db_file = tmp_path / "test_feedback.json"
    system = FeedbackSystem(str(db_file))
    
    # Act
    entry = system.submit_feedback(user_id="freelancer_1", message="The tax deduction logic is confusing.")
    
    # Assert
    assert entry.id is not None
    assert entry.user_id == "freelancer_1"
    assert entry.message == "The tax deduction logic is confusing."
    assert entry.timestamp is not None
    
    # Verify persistence
    assert db_file.exists()
    raw_data = json.loads(db_file.read_text())
    assert len(raw_data) == 1
    assert raw_data[0]["user_id"] == "freelancer_1"

def test_feedback_is_accessible(tmp_path):
    """
    Acceptance Criteria: Feedback is accessible to the product team.
    """
    # Arrange
    db_file = tmp_path / "test_feedback.json"
    system = FeedbackSystem(str(db_file))
    
    # Act - Submit multiple entries
    system.submit_feedback("user_a", "Love the new UI!")
    system.submit_feedback("user_b", "Need export to CSV feature.")
    
    # Retrieve
    all_feedback = system.get_all_feedback()
    
    # Assert
    assert len(all_feedback) == 2
    messages = [f.message for f in all_feedback]
    assert "Love the new UI!" in messages
    assert "Need export to CSV feature." in messages
    
    # Verify data integrity
    assert all_feedback[0].user_id == "user_a"
    assert all_feedback[1].user_id == "user_b"

def test_empty_state_handling(tmp_path):
    """Ensure the system handles an empty/new database correctly."""
    db_file = tmp_path / "empty_feedback.json"
    system = FeedbackSystem(str(db_file))
    
    feedbacks = system.get_all_feedback()
    assert feedbacks == []
    assert db_file.exists() # File should be created on init
