# Spark Brain v1 — Retired Architecture

**Status:** Retired  
**Retired by:** [`ADR-0002`](../../02-governance/architecture-decisions/ADR-0002-spark-brain-control-plane.md)

Spark Brain v1 was installed through commits `8956d807fc851af671f7725db1383749d8d82000` to `b61b3e52947d0b592c379ca26ddc79b252bf40b1`.

It introduced:

- business and product architecture under `/brain`
- working agreements and compatibility pointers under `/meta`
- a second ADR system under `/adr`

The files were materially complete, but the model created competing authorities alongside the existing Philosophy, Governance, Canon, Academy, and architecture-decision structure.

Spark Brain v2 retains only repository operating responsibilities: startup, navigation, current state, session continuity, machine-readable authority mapping, and integrity validation.

The retired files are not copied into this archive because doing so would preserve duplicate concepts in the working tree. Their exact contents and evolution remain available through Git history.

This archive record is historical context only and is not authoritative for current repository operation.