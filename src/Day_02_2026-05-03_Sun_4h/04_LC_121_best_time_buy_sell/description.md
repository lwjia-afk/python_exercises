# LC 121 — Best Time to Buy and Sell Stock

- **Source**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- **Difficulty**: Easy
- **Time budget**: ~25 min

## Objective
Single-pass O(n) — track min so far + best profit.

## Task
Given `prices` where `prices[i]` is the price on day `i`, return the maximum profit from one buy + one sell. If no profit is possible, return 0.

Single pass:
- `min_price = +inf`
- For each price: update `min_price`; update `max_profit = max(max_profit, price - min_price)`.

Note how this is structurally similar to Kadane (LC 53).

## Expected output
Pass on `[7,1,5,3,6,4] → 5`, `[7,6,4,3,1] → 0`.

## Self-check
What if you could do unlimited transactions? (LC 122 — different problem.)
