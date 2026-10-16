# Week 4 — AI log

## Assistant used and the screen I asked for

Claude 3.5 Sonnet. I asked for the HTML and CSS prototype of the kitchen preparation logging screen (`prep.html`) and its confirmation/cancellation flow (`prep_cancel.html`) for KitchenOps.

## My criteria, written before the prompt

Before writing the prompt, I extracted the target requirements and test cases from `week02/requirements.json` and `week04/test_cases.json`:
- REQ-002: A kitchen chef logs prepared dish portions on mobile, and the server automatically deducts raw ingredient stocks based on the recipe bill of materials. Acceptance: Logging 10 portions of a recipe containing 120g pasta and 80g sauce deducts exactly 1.2kg pasta and 0.8kg sauce from active stock.
- REQ-004: Ingredients nearing shelf-life expiration enforce FIFO rotation; batches expiring within 48 hours display an alert banner and are depleted first.
- REQ-006: Every screen is usable on a phone about 390 px wide without horizontal scrolling.
- TC-002-01: Log 10 portions of Rigatoni Pomodoro to deplete raw ingredients.
- TC-002-02: Prevent or revert accidental portion logging without corrupting inventory balance.

Things I planned to check in the assistant's answer:
1. Pure semantic HTML and vanilla CSS (no external JS frameworks, no complex build steps).
2. Clean mobile viewport scaling strictly fitting within 390 px width without horizontal scrolling.
3. Precise mathematical deduction of raw stock (1.2 kg pasta, 0.8 kg sauce base).
4. Error handling and reversibility: allowing the chef to cancel an accidental entry before or after confirmation.

## What the answer met, what it broke, what it added

- **What it met:** The assistant generated valid HTML5 markup with the standard viewport meta tag, a recipe select dropdown, and calculated the correct raw ingredient deductions for 10 portions of Rigatoni Pomodoro.
- **What it broke:** The assistant provided a one-way irreversible submit action labeled **Confirm & Deplete Stock** with zero ability to cancel or undo an erroneous submission. When my collaborator tester (220504023) tested the prototype, they noted: "If a chef accidentally enters 100 portions instead of 10, there is no button to revert or cancel this." This caused TC-002-02 to fail during the round 1 walk-through. Furthermore, the assistant formatted the ingredient deduction summary using **`<table class="data-table">`** with wide fixed columns that triggered horizontal scrollbars on a 390 px viewport, breaking REQ-006.
- **What it added:** The assistant invented an unrequested nutritional calculation card displaying **Estimated Calories: 620 kcal per serving** and macronutrient splits, which no kitchen inventory requirement asked for.

## What I changed

1. I stripped out the unrequested calorie and nutritional estimation card.
2. I converted the wide table structure into a responsive card layout with flex rows (`.item-row`), ensuring zero horizontal overflow on a 390 px phone screen to satisfy REQ-006.
3. To address the collaborator's finding for REQ-002 and TC-002-02, I built a dedicated cancellation screen (`prep_cancel.html`) and connected it to `prep_success.html` and `prep.html` via an "Undo / Cancel This Entry" button. This allows cooks to immediately revert accidental prep logs and reinstate raw stock balances.
4. My collaborator re-tested this flow in Round 2, and TC-002-02 passed. I documented this fix in `PROPOSAL.md` Change log: "2026-10-15 — REQ-002, TC-002-02: Collaborator geri bildirimi doğrultusunda hatalı porsiyon girişlerini geri almayı sağlayan prep_cancel.html akışı eklendi; ikinci tur yürütmesi başarıyla doğrulandı."

## Evidence — the actual exchange

```text
ME:
I am building a clickable mobile prototype for KitchenOps (commercial kitchen inventory depletion).
Create the prototype screen prep.html for logging prepared dishes.
It must satisfy:
- REQ-002: Logging prepared dish portions deducts raw ingredients via recipe BOM. Specifically, 10 portions of Rigatoni Pomodoro (120g pasta, 80g sauce per portion) must deduct 1.2 kg pasta and 0.8 kg sauce.
- REQ-004: FIFO batch rotation indicator showing oldest batch is depleted first.
- REQ-006: Usable on a 390 px wide phone without horizontal scrolling.
Include test case verification for TC-002-01. Plain HTML and CSS only.

AI:
Here is the HTML prototype for prep.html:

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>KitchenOps - Prep</title>
<style>
.data-table { width: 480px; border-collapse: collapse; }
</style>
</head>
<body>
<!-- serves: REQ-002, REQ-004, REQ-006 -->
<div class="phone">
  <h2>Log Prepared Dishes</h2>
  <form action="prep_success.html">
    <label>Recipe</label>
    <select name="recipe">
      <option value="rigatoni">Rigatoni Pomodoro</option>
    </select>
    <label>Portions</label>
    <input type="number" value="10">
    
    <table class="data-table">
      <tr><th>Ingredient</th><th>Qty</th><th>BOM Rate</th></tr>
      <tr><td>Pasta</td><td>-1.2 kg</td><td>120g/portion</td></tr>
      <tr><td>Sauce</td><td>-0.8 kg</td><td>80g/portion</td></tr>
    </table>
    
    <div class="nutrition-card">
      <p>Estimated Calories: 620 kcal per serving</p>
    </div>
    
    <button type="submit">Confirm & Deplete Stock</button>
  </form>
</div>
</body>
</html>
```
