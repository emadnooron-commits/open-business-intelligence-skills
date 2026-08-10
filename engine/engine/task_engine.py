from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


TASK_STATES = {
    "CREATED",
    "QUEUED",
    "SCHEDULED",
    "BLOCKED",
    "AWAITING_APPROVAL",
    "RUNNING",
    "VALIDATING",
    "COMPLETED",
    "FAILED",
    "RETRY",
    "ESCALATED",
    "CANCELLED",
}


@dataclass
class Task:
    task_id: str
    goal_id: str
    title: str
    objective: str

    priority: str = "MEDIUM"
    status: str = "CREATED"

    assigned_agent: Optional[str] = None

    dependencies: List[str] = field(default_factory=list)
    required_skills: List[str] = field(default_factory=list)
    required_tools: List[str] = field(default_factory=list)

    input_data: Dict[str, Any] = field(default_factory=dict)
    expected_output: Optional[str] = None
    actual_output: Optional[Any] = None

    validation_rules: List[str] = field(default_factory=list)
    evidence: List[Any] = field(default_factory=list)

    retry_limit: int = 3
    retry_count: int = 0

    failure_reason: Optional[str] = None

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def set_status(self, new_status: str) -> None:
        if new_status not in TASK_STATES:
            raise ValueError(f"Invalid task status: {new_status}")

        self.status = new_status

    def can_retry(self) -> bool:
        return self.retry_count < self.retry_limit

    def retry(self) -> bool:
        if not self.can_retry():
            self.set_status("ESCALATED")
            return False

        self.retry_count += 1
        self.set_status("RETRY")
        return True

    def complete(self, output: Any, evidence: Optional[List[Any]] = None):
        self.actual_output = output

        if evidence:
            self.evidence.extend(evidence)

        self.set_status("COMPLETED")

    def fail(self, reason: str):
        self.failure_reason = reason
        self.set_status("FAILED")

    def is_ready(self, completed_tasks: List[str]) -> bool:
        return all(
            dependency in completed_tasks
            for dependency in self.dependencies
        )


class TaskEngine:
    """
    Minimal foundation for the NOOR AI OS task engine.

    This layer manages task state and readiness.
    Scheduling and Agent execution are handled by other components.
    """

    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def add_task(self, task: Task) -> None:
        if task.task_id in self.tasks:
            raise ValueError(
                f"Task already exists: {task.task_id}"
            )

        self.tasks[task.task_id] = task

    def get_task(self, task_id: str) -> Task:
        if task_id not in self.tasks:
            raise KeyError(f"Task not found: {task_id}")

        return self.tasks[task_id]

    def ready_tasks(self) -> List[Task]:
        completed = [
            task.task_id
            for task in self.tasks.values()
            if task.status == "COMPLETED"
        ]

        return [
            task
            for task in self.tasks.values()
            if task.status in {"CREATED", "QUEUED", "RETRY"}
            and task.is_ready(completed)
        ]

    def queue_task(self, task_id: str) -> None:
        task = self.get_task(task_id)
        task.set_status("QUEUED")

    def cancel_task(self, task_id: str) -> None:
        task = self.get_task(task_id)
        task.set_status("CANCELLED")
