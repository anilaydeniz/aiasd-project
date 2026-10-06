# Week 2 — AI log

**What I used AI for**

I prompted both Claude 3.5 Sonnet and ChatGPT-4o with my PROPOSAL.md §3 (Problem) and §4 (Solution) descriptions, asking them to generate eight candidate software requirements (five functional, three non-functional) with priorities (must/should/could) and acceptance criteria.

**What it got right**

Both models identified the necessity of recipe-based Bill of Materials (BOM) deduction upon dish completion (REQ-002) and automated purchase order generation when inventory crosses minimum safety thresholds (REQ-003). Claude also accurately formulated the 48-hour FIFO batch expiration warning mechanism.

**What it got wrong, or what I had to correct**

ChatGPT-4o hallucinated a customer-facing payment requirement: "The mobile app integrates with Stripe POS terminal so diners can pay their dinner bills at the table and tip the server." This directly violates the explicit non-goal stated in PROPOSAL.md §4: *"KitchenOps deliberately does NOT process customer POS dining payments, handle kitchen display ticket routing, or manage delivery courier dispatch."* Additionally, ChatGPT marked all eight generated requirements as "must", defeating prioritization. I discarded the POS billing feature, introduced the inbound crate receiving requirement (REQ-005), and balanced the priorities across four musts, three shoulds, and one could.

**Evidence — the actual exchange**

```text
User: Here is §3 and §4 of KitchenOps: <pasted Problem and Solution>. Write 8 software requirements (5 functional, 3 non-functional) with priorities and acceptance criteria.

ChatGPT:
1. POS Payment Integration (Priority: Must)
   The mobile application integrates with Stripe and physical POS terminals allowing restaurant patrons to tap their credit cards and settle table tabs directly.
   Acceptance: Customer credit card payment succeeds within 3 seconds and issues digital receipt.
2. Recipe Stock Deduction (Priority: Must)
   ...
All 8 requirements marked Must priority for complete enterprise kitchen readiness.
```

**How I noticed**

I compared the generated requirements directly against the scope boundary in PROPOSAL.md §4. The proposal explicitly confines the product to back-of-house kitchen storage and wholesale supplier replenishment. A dining payment gateway would add unnecessary PCI compliance and payment terminal hardware dependencies to a 10-week student project.

**What I learned this week**

When prompting language models for software requirements, specifying negative constraints ("what the product deliberately does NOT do") is just as critical as describing desired features; otherwise, models reflexively append generic industry features that bloat project scope.
