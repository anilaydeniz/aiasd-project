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
10. **`prep_cancel.html`** (REQ-002, REQ-006) — Revert & cancellation screen for accidental prep portions (#TX-9042) to restore depleted ingredient stocks.
11. **`batch_expiry.html`** (REQ-004, REQ-006) — Physical shelf location and FIFO batch tracking screen with 48h spoilage alerts.

---

## Invented Data

- **Staff E-mail:** `chef@kitchenops.internal`
- **Valid Login Code:** `1234`
- **Invalid Login Code:** `0000` (triggers "Wrong code" error)
- **Active Prep Recipe:** `Rigatoni Pomodoro` (BOM portion formula: 120g pasta, 80g tomato sauce per portion)
- **Standard Prep Batch:** `10 portions` (deducts exactly `1.2 kg` pasta and `0.8 kg` tomato sauce from active batches #P-201 and #S-108)
- **Prep Cancellation:** `#TX-9042` reversible action reinstating `+1.2 kg` pasta and `+0.8 kg` tomato sauce
- **Low-Stock Trigger Item:** Cooking Cream at `3.5 L` (safety threshold: `5.0 L`, deficit: `-1.5 L`)
- **Automated Purchase Order:** `PO-2026-041` for `20.0 L` Cooking Cream (4 crates × 5L) to Wholesale Dairy & Produce Logistics Ltd.
- **Expiring FIFO Batch:** Cooking Cream `Lot #B-104` expiring in `36 hours` (amber alert banner displayed)
- **Physical Storage Shelf Locations:**
  - *Walk-in Chiller #1 — Shelf B-03:* Cooking Cream Lot #B-104 (3.5 L)
  - *Walk-in Chiller #1 — Shelf A-01:* Mozzarella Cheese Lot #M-409 (4.0 kg)
  - *Dry Pantry Kiosk — Shelf D-12:* Rigatoni Pasta Lot #P-201 (13.3 kg)
  - *Dry Pantry Kiosk — Shelf D-08:* Tomato Sauce Base Lot #S-108 (7.4 kg)
- **Inbound Goods Delivery:** `25 kg` All-Purpose Flour bag, Batch `LOT-FL-20261013`, expiry date `2027-04-15`

---

## Walk-Through Instructions for Testers

1. **Open in Browser:** Double-click `index.html` to open in Chrome or Edge.
2. **Device Viewport:** Press `F12`, click the mobile device simulation icon (`Ctrl+Shift+M` / `Cmd+Shift+M`), and set the viewport width to `390 px`.
3. **Execute Test Cases:** Follow the step-by-step actions in `week04/test_cases.json`:
   - `TC-001-01`: Enter `chef@kitchenops.internal` and code `1234` to access the main station dashboard.
   - `TC-002-01`: Log 10 portions of Rigatoni Pomodoro to verify the 1.2 kg pasta / 0.8 kg sauce depletion audit log.
   - `TC-003-01`: Open Purchase Orders and dispatch the 20-liter replenishment PO for cooking cream.
   - `TC-004-01`: Verify that the amber 48-hour FIFO alert is displayed on Live Inventory for Lot #B-104.
   - `TC-002-02 (Round 2)`: From `prep_success.html`, tap "Undo / Cancel This Entry" to verify `prep_cancel.html` successfully reverts the stock deduction.

---

## Session & Walk-Through Testing Summary

- **In-Class Date:** October 13, 2026
- **Collaborator Tester:** Student ID `220504023`
- **Executed Test Cases:**
  - `TC-001-01` (OTP login flow): **PASS**
  - `TC-002-01` (Log 10 portions Rigatoni Pomodoro): **PASS**
  - `TC-003-01` (Low cream stock auto-generates PO): **PASS**
  - `TC-002-02 (Round 1)`: **FAIL** *(Collaborator noted missing cancel/undo button)*
  - `TC-002-02 (Round 2)`: **PASS** *(Resolved via prep_cancel.html screen and confirmed by collaborator)*
- **Deliverables Status:** All in-class (18/18) and weekend round 2 verification tests confirmed.
