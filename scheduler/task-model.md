# NOOR AI OS — Task Model

## Purpose

The Task Model defines the standard structure of every executable task in NOOR AI OS.

A task is the smallest meaningful unit of work that an Agent can execute and validate.

---

## Task Lifecycle

CREATED
↓
QUEUED
↓
SCHEDULED
↓
RUNNING
↓
VALIDATING
↓
COMPLETED

Failure:

RUNNING
↓
FAILED
↓
RETRY
↓
RUNNING

Repeated failure:

FAILED
↓
ESCALATED
↓
HUMAN REVIEW

---

## Required Task Fields

Every task should contain:

### Identity

- task_id
- goal_id
- parent_task_id

### Definition

- title
- objective
- description

### Input

- input_data
- context
- required_information

### Execution

- assigned_agent
- required_skills
- required_tools

### Priority

- priority
- urgency
- business_impact
- risk

### Scheduling

- created_at
- scheduled_at
- deadline

### Dependencies

- dependencies
- blocking_tasks

### Output

- expected_output
- actual_output
- evidence

### Validation

- validation_rules
- validation_status
- validator

### Failure Handling

- retry_limit
- retry_count
- failure_reason
- escalation_required

### Status

- status

Possible values:

CREATED
QUEUED
SCHEDULED
RUNNING
VALIDATING
COMPLETED
FAILED
RETRY
ESCALATED
CANCELLED

---

## Example Task

### Goal

Launch a new NOOR compressed charcoal product.

### Task

Research competitors in the Egyptian compressed charcoal market.

### Structured Definition

```text
task_id:
NOOR-MKT-001

goal_id:
NOOR-PRODUCT-LAUNCH-001

title:
Research Egyptian compressed charcoal competitors

objective:
Identify major competitors, products, prices, positioning and market gaps.

assigned_agent:
Research Agent

required_skills:
- Market Research
- Competitor Analysis
- Data Analysis

required_tools:
- Web Research
- Data Collection

priority:
HIGH

business_impact:
HIGH

risk:
LOW

expected_output:
A structured competitor analysis report.

validation_rules:
- Sources must be identified.
- Prices must include date/context.
- Competitors must be clearly differentiated.
- Claims must be supported by evidence.

status:
CREATED
