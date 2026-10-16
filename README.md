# Asphalt Math

Honest driveway-sealer arithmetic. The pail claims four hundred square feet; Asphalt Math
counts the gallons, the weathered thirst and the crack tubes the driveway was always going
to ask for.

## What it does

Three panels of hypothetical arithmetic on labeled norms:

- **The coverage truth** - area times coats against the claimed coverage: the honest gallon count.
- **The thirst truth** - weathered asphalt drinks more than the lab floor did: the thirst norm, priced in gallons.
- **The crack truth** - linear feet of cracks against the tube claim: whole tubes.

## The boundary

Asphalt Math keeps coverage, thirst and crack arithmetic only. Every coverage, thirst and
filler figure is a labeled norm, not a promise - surface condition, temperature and weather
change real results. Follow the sealer's label, respect its cure and weather windows, and
never take this page's word over the manufacturer's instructions. Every figure is hypothetical
arithmetic on labeled norms, not a statement about any real sealer, filler or driveway.

## Files

- `index.html` - landing page
- `app.html` - the app
- `engine.js` - the arithmetic (shared by the page and the tests)
- `oracle.py` - a Python mirror of the engine, float for float
- `expected.json` - oracle output for its inline cases
- `test.js` - runs the engine against `expected.json`

## Test

```
python3 oracle.py   # regenerates expected.json
node test.js        # 25 cases / 25 checks, 0 failed
```
