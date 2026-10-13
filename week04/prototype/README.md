# KitchenOps Clickable Prototype

A clickable mobile-first prototype demonstrating the core workflows of KitchenOps before backend integration.

**The rules**

- One HTML file for each screen, all in this folder. `index.html` is the first screen.
- It opens with a double click on `index.html`: no server, no framework, no build step. Plain HTML, shared `style.css`, and minimal client-side JavaScript.
- Every screen can be reached from `index.html` by clicking, and every link leads to a screen that exists.
- Every screen has a comment near the top specifying the requirements it serves: `<!-- serves: REQ-002, REQ-006 -->`.
- The prototype is designed for a phone view about 390 px wide (no horizontal scrolling).
- Consistent invented data across all screens for reproducible walk-through testing.

---

## Screen Flow

1. **`index.html`** (REQ-001, REQ-006) — Staff e-mail login screen.
2. **`code.html`** (REQ-001, REQ-006) — 4-digit OTP verification code screen (valid code: `1234`).
3. **`home.html`** (REQ-002, REQ-004, REQ-006) — Central KitchenOps station dashboard with urgent alerts and main workflow links.
4. **`prep.html`** (REQ-002, REQ-006) — Log prepared dishes and view dynamic recipe bill of materials stock depletion.
5. **`prep_success.html`** (REQ-002, REQ-006) — Confirmation audit log screen showing deducted ingredient quantities.
6. **`inventory.html`** (REQ-004, REQ-006) — Live walk-in inventory dashboard with FIFO batch tracking and 48-hour expiration warning.
7. **`order.html`** (REQ-003, REQ-006) — Automated supplier purchase order triggered by stock falling below safety threshold.
8. **`order_success.html`** (REQ-003, REQ-006) — Confirmation screen for dispatched wholesale purchase order.
9. **`receiving.html`** (REQ-005, REQ-006) — Inbound goods receiving screen for newly delivered crates with batch lot dates.

---

## Invented Data

- **Staff E-mail:** `chef@kitchenops.internal`
- **Valid Login Code:** `1234`
- **Invalid Login Code:** `0000` (triggers "Wrong code" error)
- **Active Prep Recipe:** `Rigatoni Pomodoro` (BOM portion formula: 120g pasta, 80g tomato sauce per portion)
- **Standard Prep Batch:** `10 portions` (deducts exactly `1.2 kg` pasta and `0.8 kg` tomato sauce from active batches #P-201 and #S-108)
- **Low-Stock Trigger Item:** Cooking Cream at `3.5 L` (safety threshold: `5.0 L`, deficit: `-1.5 L`)
- **Automated Purchase Order:** `PO-2026-041` for `20.0 L` Cooking Cream (4 crates × 5L) to Wholesale Dairy & Produce Logistics Ltd.
- **Expiring FIFO Batch:** Cooking Cream `Lot #B-104` expiring in `36 hours` (amber alert banner displayed)
- **Inbound Goods Delivery:** `25 kg` All-Purpose Flour bag, Batch `LOT-FL-20261013`, expiry date `2027-04-15`
