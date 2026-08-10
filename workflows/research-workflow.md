# NOOR AI OS — Research Workflow

## Purpose

This workflow connects the Scheduler, Research Agent and Supervisor Agent into one controlled execution cycle.

The workflow converts a research task into a validated business result.

---

## Workflow

TASK
↓
SCHEDULER
↓
RESEARCH AGENT
↓
RESEARCH RESULT
↓
SUPERVISOR
↓
DECISION

APPROVED → COMPLETED
REVISION → RESEARCH AGENT
REJECTED → RETRY
ESCALATED → HUMAN REVIEW

---

## Step 1 — Task Intake

The Scheduler receives a research task.

Example:

"Analyze the Egyptian compressed charcoal market."

The Scheduler checks:

- task_id
- goal_id
- objective
- priority
- deadline
- dependencies
- required skills
- validation rules

---

## Step 2 — Readiness Check

Before execution, the Scheduler verifies:

- Required information is available.
- Dependencies are completed.
- Research Agent is available.
- Required tools are available.
- The task is authorized.

If requirements are missing:

STATUS = BLOCKED

The task must not start.

---

## Step 3 — Agent Assignment

The Scheduler assigns the task to:

Research Agent

The Agent receives:

- Objective
- Context
- Inputs
- Expected output
- Deadline
- Validation rules

---

## Step 4 — Research Execution

The Research Agent performs:

1. Research planning
2. Source discovery
3. Data collection
4. Source verification
5. Analysis
6. Synthesis

The Agent records important evidence.

---

## Step 5 — Result Submission

The Research Agent returns a structured result containing:

- Executive Summary
- Findings
- Evidence
- Sources
- Opportunities
- Risks
- Recommendations
- Limitations

The result is sent to the Supervisor.

---

## Step 6 — Supervisor Review

The Supervisor evaluates:

- Accuracy
- Completeness
- Evidence
- Relevance
- Consistency
- Risk
- Requirements

The Supervisor returns one decision:

APPROVED
REVISION_REQUIRED
REJECTED
ESCALATED

---

## Step 7 — Approved

If approved:

```text
Task Status = COMPLETED
