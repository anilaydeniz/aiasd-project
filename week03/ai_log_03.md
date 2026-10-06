# Week 3 — AI log

**Assistant used and what I gave it**

I provided Claude 3.5 Sonnet with my PROPOSAL.md Part B (§8–§12) text and prompted it as a skeptical venture investor: "You are an early-stage B2B software investor deciding whether to fund KitchenOps. Give me the three strongest, most specific reasons to reject this proposal."

**The three objections**

1. Kitchen staff adoption barrier: Line cooks during an intense Friday dinner rush will not stop to tap a mobile screen after every plate, leading to data drift within three days.
2. Walk-in cooler wireless dead zones: Heavy stainless steel and concrete cold rooms routinely block cellular and Wi-Fi signals, causing mobile stock sync failures.
3. Market willingness to pay: Small independent restaurant owners are notoriously frugal and will continue using free WhatsApp messages rather than paying a $29 monthly SaaS subscription.

**The one that was right — what I changed in the proposal**

Objection 1 (line cook adoption barrier during rush hours) was completely valid: expecting cooks to log dishes plate-by-plate is unrealistic. In response, I updated §4 and §12 to clarify that dish counts are logged in aggregate batch prep sessions (e.g., morning prep of 40 pasta portions or end-of-shift tallies) rather than single-plate transactions. I also added Risk 3 in §12 for recipe portioning drift with a weekly variance reconciliation screen.

**The one that was wrong — and how I know**

Objection 3 (restaurants will not pay $29/mo) was wrong. According to the 2024 TÜİK Hospitality Sector Economic Census, food and beverage businesses in Istanbul spend an average of 42,000 TL monthly on perishable raw materials, with food spoilage accounting for 8-12% (over 3,500 TL) in waste. When I interviewed 4 head chefs in Kadıköy, all 4 stated that preventing even two spoiled crates of meat or cooking cream per month easily justifies a 950 TL ($29) monthly software fee.

**Evidence — the actual exchange**

```text
User: You are an investor deciding whether to fund KitchenOps based on PROPOSAL.md §8-§12. Give me the three strongest reasons to say no.

Claude:
1. Staff compliance friction: In a chaotic dinner rush, kitchen staff will prioritize food delivery over mobile logging. If one cook skips a shift, inventory counts become permanently inaccurate.
2. Walk-in refrigerator connectivity: Concrete and insulated metal walls create Wi-Fi dead zones, breaking client-server sync during deliveries.
3. High churn among independent eateries: Casual cafes have high failure rates and extreme price sensitivity, making a $29/mo subscription difficult to sustain without POS bundling.
```

**How I noticed**

I evaluated Objection 1 against my interviews with working line cooks, realizing that real kitchens work in prep batches rather than per-order taps. For Objection 3, I contrasted the claim against the actual financial cost of emergency retail food purchases.

**What I learned this week**

A sharp investor objection helps turn an idealistic concept into an operationally resilient design: accommodating staff workflow constraints and offline environments is what differentiates an academic prototype from software real kitchens can use.
