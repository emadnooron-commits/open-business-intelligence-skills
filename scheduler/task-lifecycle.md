# NOOR AI OS — Task Lifecycle

## Purpose

This document defines how a task moves through the NOOR AI OS from creation to completion.

The Scheduler controls the lifecycle.

---

# 1. CREATED

The task has been created but has not yet entered the execution queue.

The system checks:

- Is the objective clear?
- Is the expected output defined?
- Is an Agent available?
- Are required inputs available?
- Are dependencies defined?
- Are validation rules defined?

If the task is incomplete, it remains in CREATED.

---

# 2. QUEUED

The task is ready for scheduling.

The Scheduler places it into the appropriate queue according to:

- Priority
- Urgency
- Business impact
- Dependencies
- Available resources

---

# 3. SCHEDULED

The Scheduler has selected:

- Execution time
- Agent
- Required tools
- Execution priority

The task is now waiting for execution.

---

# 4. RUNNING

The assigned Agent begins execution.

The system records:

- Start time
- Agent
- Tools used
- Inputs
- Actions
- Intermediate results

---

# 5. VALIDATING

The Agent has produced an output.

The Validator checks:

- Completeness
- Accuracy
- Evidence
- Requirements
- Output format
- Logical consistency

The task cannot become COMPLETED without successful validation.

---

# 6. COMPLETED

The task has:

- Been executed
- Produced the expected output
- Passed validation
- Stored its result
- Recorded evidence

The system updates dependent tasks.

---

# 7. FAILED

A task enters FAILED when execution cannot produce an acceptable result.

Possible causes:

- Missing information
- Tool failure
- Agent failure
- Invalid input
- External service failure
- Validation failure
- Unexpected condition

The system records the failure reason.

---

# 8. RETRY

The Scheduler may retry a failed task.

Before retrying, the system should determine whether the failure can be corrected.

Possible corrections:

- Change Agent
- Change tool
- Improve input
- Add missing information
- Modify instructions
- Reduce task scope

The system must not repeat the exact same failed execution indefinitely.

---

# 9. ESCALATED

A task becomes ESCALATED when:

- Retry limit is reached
- Risk is high
- Agents disagree
- Required information is unavailable
- Human judgment is required
- The task exceeds Agent permissions

The Supervisor Agent reviews the task.

If necessary, it is sent to human leadership.

---

# 10. CANCELLED

A task may be cancelled when:

- The parent goal is cancelled
- The task is no longer relevant
- A better strategy replaces it
- Human leadership cancels it
- The task becomes invalid

Cancelled tasks remain in the audit history.

---

# State Machine

```text
CREATED
   |
   v
QUEUED
   |
   v
SCHEDULED
   |
   v
RUNNING
   |
   v
VALIDATING
   |
   +------------------+
   |                  |
   v                  v
COMPLETED           FAILED
                       |
                       v
                     RETRY
                       |
                       v
                    RUNNING

FAILED
   |
   v
ESCALATED
   |
   v
SUPERVISOR / HUMAN
