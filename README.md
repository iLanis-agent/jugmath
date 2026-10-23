# Jug Math

Event water jug bundle, week, cost and time arithmetic. The 520 jugs at 6 jugs a bundle take 87 bundles, the last bundle holding 4 jugs.

## Named constants

None. Every number is the owner's own entry.

## What it computes

- **The bundles truth** - the jugs (1 to 1000000) divided by the jugs a bundle (1 to 1000), rounded up, with what the last bundle holds.
- **The weeks truth** - the jugs divided by the jugs used a week (1 to 100000), with the jugs left for the next week.
- **The cost truth** - the bundles (1 to 100000) times the bundle price ($0.01 to $999.99) to the cent, and spread over the jugs, half rounded up.
- **The time truth** - the jugs divided by the jugs filled a minute (1 to 100), rounded up, in minutes and in hours and minutes.

## Boundary

Arithmetic only. Counting applied as written. It has not seen any jug, bundle or cooler and does not know whether the water will really arrive cold, a supplier will run out or a price will hold, and it gives no verdict that a bundle is worth its price or a jug is right for an event. Every number is the owner's own entry.

## Files

- `index.html` - landing page with the boundary and starting examples.
- `app.html` - the calculator; every bundle recomputes on each keystroke.
- `engine.js` - the four truths, shared by the page and the tests.
- `oracle.py` - an independent Python re-implementation; writes `expected.json`.
- `test.js` - runs the engine against `expected.json` (99 cases, 20 error cases).

## Tests

```
python3 oracle.py
node test.js
```
