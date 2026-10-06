---
marp: true
paginate: true
---

# KitchenOps

**Commercial kitchen inventory depletion and smart restock logistics.**

Anıl Aydeniz · Software Engineering · Week 3

---

## 1. The last time it happened — to me, or in front of me

- **When:** September 18, 2026, around 20:45 during dinner rush.
- **Who / where / doing what:** A line cook at a busy Italian bistro in Kadıköy running out of heavy cooking cream while preparing 14 pending pasta orders.
- **What they did instead:** The head chef had to sprint to the corner supermarket to buy 10 small retail cartons at 45 TL each instead of the 24 TL wholesale price.
- **What it cost:** 35 minutes of delayed orders, 3 table cancellations, and 210 TL direct retail markup penalty.

---

## 2. Five people who will test it in Week 9

| # | Name | How you know them | Why they have the same problem |
|---|------|-------------------|--------------------------------|
| 1 | Emre Yılmaz | High school friend working as cafe line cook | Runs out of espresso milk during morning rush |
| 2 | Caner Aksoy | Cousin managing a neighborhood burger restaurant | Loses fresh buns and burger patties to cold-room spoilage |
| 3 | Burak Demir | Classmate working part-time at campus cafeteria | Frustrated by late-night clipboard inventory audits |
| 4 | Selin Kaya | University club teammate with catering family | Experiences supply shortages during weekend banquets |
| 5 | Mert Öztürk | Former dormitory roommate working at bakery | Throws away expired dairy due to unorganized batch rotation |

---

## 3. What it does — and what it does not

1. REQ-002 — A kitchen chef logs prepared dish portions on mobile, and the server automatically deducts raw ingredient stocks based on the recipe bill of materials.
2. REQ-003 — When an ingredient's stock level drops below its safety threshold, the server automatically appends the required replenishment quantity to the active supplier purchase order.
3. REQ-004 — The system tags inbound ingredient crates with batch arrival and expiration dates, enforcing First-In First-Out (FIFO) usage priority and alerting staff 48 hours prior to spoilage.

**It does not:** process customer POS dining payments, handle kitchen display ticket routing, or manage delivery courier dispatch.

---

## 4. The main screen

```text
+------------------------------------------+
|  KitchenOps — Live Kitchen Stock         |
+------------------------------------------+
|  [!] 2 Batches Expiring (FIFO Warning)   |
|  - Heavy Cream (Batch #104) : 18h left   |
+------------------------------------------+
|  Inventory Levels:                       |
|  - Penne Pasta    : 14.5 kg  [Normal]    |
|  - Tomato Puree   :  3.2 kg  [LOW - PO]  |
|  - Beef Tenderloin:  8.0 kg  [Normal]    |
+------------------------------------------+
|  [ + Log Prepared Dishes ]               |
|  [ View Supplier Purchase Order (3) ]    |
+------------------------------------------+
```

---

## 5. What I am not sure about

**How should the system resolve recipe yield variance when cooks slightly over-portion ingredients?**

Real-world line cooks do not weigh every pinch of salt or splash of oil down to the exact gram during a busy service. I worry that variance between theoretical recipe deductions and physical kitchen reality might accumulate over two weeks, requiring periodic reconciliation counts.

---

## 6. Reviewers — answer these three, in writing

1. **Real?** Did they convince you this problem happens to them, and to the five people on slide 2?
2. **Usable here?** Could those five people actually use this in Week 9 — what would stop them?
3. **Too much or too little?** Which part will not be finished by Week 11 — or has the product shrunk to one screen?
