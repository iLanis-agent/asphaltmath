import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def coverage_truth(area, claim, coats):
    if not (area > 0):
        raise ValueError("the area must be above zero")
    if not (claim > 0):
        raise ValueError("the claimed coverage must be above zero")
    if not (coats > 0):
        raise ValueError("the coats must be above zero")
    gallons = area * coats / claim
    rounded = math.floor(gallons * 10 + 0.5) / 10
    if rounded <= 2:
        verdict = "a bucket or two honestly"
    elif rounded <= 5:
        verdict = "a five-gallon pail honestly"
    elif rounded <= 15:
        verdict = "a few pails honestly"
    else:
        verdict = "a drum order honestly"
    return f"{area} {plural(area, 'square foot', 'square feet')} at {coats} {plural(coats, 'coat', 'coats')} of the {claim}-square-foot claim is {fixed1(gallons)} {plural(1 if rounded == 1 else 2, 'gallon', 'gallons')} - {verdict}."

def thirst_truth(area, claim, thirst):
    if not (area > 0):
        raise ValueError("the area must be above zero")
    if not (claim > 0):
        raise ValueError("the claimed coverage must be above zero")
    if not (thirst >= 0):
        raise ValueError("the thirst norm must be zero or more")
    base = area / claim
    gallons = base * (1 + thirst / 100)
    extra = gallons - base
    rounded_extra = math.floor(extra * 10 + 0.5) / 10
    if rounded_extra == 0:
        tail = "no real thirst honestly."
    else:
        if rounded_extra <= 0.5:
            verdict = "a light thirst honestly"
        elif rounded_extra <= 2:
            verdict = "a working thirst honestly"
        else:
            verdict = "a deep thirst honestly"
        tail = f"{fixed1(extra)} extra {plural(1 if rounded_extra == 1 else 2, 'gallon', 'gallons')} of thirst, {verdict}."
    rounded_gal = math.floor(gallons * 10 + 0.5) / 10
    return f"{area} {plural(area, 'square foot', 'square feet')} of weathered asphalt at the {thirst}% thirst norm drinks {fixed1(gallons)} {plural(1 if rounded_gal == 1 else 2, 'gallon', 'gallons')} a coat - {tail}"

def crack_truth(feet, tube):
    if not (feet > 0):
        raise ValueError("the crack length must be above zero")
    if not (tube > 0):
        raise ValueError("the tube claim must be above zero")
    tubes = math.ceil(feet / tube - 1e-9)
    if tubes == 1:
        verdict = "a single tube honestly"
    elif tubes <= 4:
        verdict = "a handful of tubes honestly"
    elif tubes <= 10:
        verdict = "a box of tubes honestly"
    else:
        verdict = "a case honestly"
    return f"{feet} linear {plural(feet, 'foot', 'feet')} of cracks against the {tube}-foot tube claim is {tubes} {plural(tubes, 'tube', 'tubes')} - {verdict}."

FNS = {"coverageTruth": coverage_truth, "thirstTruth": thirst_truth, "crackTruth": crack_truth}

cases = [
 {"fn":"coverageTruth","args":[600,250,2]},
 {"fn":"coverageTruth","args":[200,250,1]},
 {"fn":"coverageTruth","args":[1000,300,2]},
 {"fn":"coverageTruth","args":[3000,200,2]},
 {"fn":"coverageTruth","args":[100,100,1]},
 {"fn":"coverageTruth","args":[125,250,2]},
 {"fn":"coverageTruth","args":[0,250,2]},
 {"fn":"coverageTruth","args":[600,0,2]},
 {"fn":"coverageTruth","args":[600,250,0]},
 {"fn":"thirstTruth","args":[600,250,30]},
 {"fn":"thirstTruth","args":[400,250,10]},
 {"fn":"thirstTruth","args":[2000,200,50]},
 {"fn":"thirstTruth","args":[100,250,5]},
 {"fn":"thirstTruth","args":[600,250,0]},
 {"fn":"thirstTruth","args":[600,250,-5]},
 {"fn":"thirstTruth","args":[0,250,30]},
 {"fn":"crackTruth","args":[80,30]},
 {"fn":"crackTruth","args":[25,30]},
 {"fn":"crackTruth","args":[100,30]},
 {"fn":"crackTruth","args":[300,30]},
 {"fn":"crackTruth","args":[500,30]},
 {"fn":"crackTruth","args":[1,30]},
 {"fn":"crackTruth","args":[90,30]},
 {"fn":"crackTruth","args":[0,30]},
 {"fn":"crackTruth","args":[80,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
