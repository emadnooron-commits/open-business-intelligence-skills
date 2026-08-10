# NOOR AI OS — Scheduler Rules

## Purpose

The Scheduler decides what task should run, when it should run, which Agent should execute it, and what should happen when execution fails.

---

## Scheduling Decision

For every ready task, the Scheduler evaluates:

1. Priority
2. Strategic importance
3. Deadline
4. Business impact
5. Dependencies
6. Risk
7. Required Agent
8. Available resources

---

## Priority Levels

### CRITICAL

Immediate attention.

Used for:

- Critical business operations
- Safety issues
- Severe failures
- Time-sensitive strategic matters

### HIGH

Important tasks with significant business impact.

### MEDIUM

Normal operational work.

### LOW

Tasks that can safely wait.

---

## Dependency Rule

A task cannot run while a required dependency is incomplete.

Example:

```text
Research
   ↓
Analysis
   ↓
Decision
