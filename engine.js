// Asphalt Math engine - hypothetical arithmetic on labeled norms only.
// Coverage, thirst and filler figures are illustrative norms; surface
// condition, temperature and weather change real results.

function plural(n, one, many) { return n === 1 ? one : many; }

function fixed1(x) { return (Math.floor(x * 10 + 0.5) / 10).toFixed(1); }

function coverageTruth(area, claim, coats) {
  if (!(area > 0)) throw new Error("the area must be above zero");
  if (!(claim > 0)) throw new Error("the claimed coverage must be above zero");
  if (!(coats > 0)) throw new Error("the coats must be above zero");
  const gallons = area * coats / claim;
  const rounded = Math.round(gallons * 10) / 10;
  let verdict;
  if (rounded <= 2) verdict = "a bucket or two honestly";
  else if (rounded <= 5) verdict = "a five-gallon pail honestly";
  else if (rounded <= 15) verdict = "a few pails honestly";
  else verdict = "a drum order honestly";
  return `${area} ${plural(area, "square foot", "square feet")} at ${coats} ${plural(coats, "coat", "coats")} of the ${claim}-square-foot claim is ${fixed1(gallons)} ${plural(rounded === 1 ? 1 : 2, "gallon", "gallons")} - ${verdict}.`;
}

function thirstTruth(area, claim, thirst) {
  if (!(area > 0)) throw new Error("the area must be above zero");
  if (!(claim > 0)) throw new Error("the claimed coverage must be above zero");
  if (!(thirst >= 0)) throw new Error("the thirst norm must be zero or more");
  const base = area / claim;
  const gallons = base * (1 + thirst / 100);
  const extra = gallons - base;
  const roundedExtra = Math.round(extra * 10) / 10;
  let tail;
  if (roundedExtra === 0) tail = "no real thirst honestly.";
  else {
    let verdict;
    if (roundedExtra <= 0.5) verdict = "a light thirst honestly";
    else if (roundedExtra <= 2) verdict = "a working thirst honestly";
    else verdict = "a deep thirst honestly";
    tail = `${fixed1(extra)} extra ${plural(roundedExtra === 1 ? 1 : 2, "gallon", "gallons")} of thirst, ${verdict}.`;
  }
  return `${area} ${plural(area, "square foot", "square feet")} of weathered asphalt at the ${thirst}% thirst norm drinks ${fixed1(gallons)} ${plural(Math.round(gallons * 10) / 10 === 1 ? 1 : 2, "gallon", "gallons")} a coat - ${tail}`;
}

function crackTruth(feet, tube) {
  if (!(feet > 0)) throw new Error("the crack length must be above zero");
  if (!(tube > 0)) throw new Error("the tube claim must be above zero");
  const tubes = Math.ceil(feet / tube - 1e-9);
  let verdict;
  if (tubes === 1) verdict = "a single tube honestly";
  else if (tubes <= 4) verdict = "a handful of tubes honestly";
  else if (tubes <= 10) verdict = "a box of tubes honestly";
  else verdict = "a case honestly";
  return `${feet} linear ${plural(feet, "foot", "feet")} of cracks against the ${tube}-foot tube claim is ${tubes} ${plural(tubes, "tube", "tubes")} - ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { coverageTruth, thirstTruth, crackTruth };
}
