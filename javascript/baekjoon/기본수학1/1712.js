const { input } = require('../input');

const [fixedCost, variableCost, sellingCost] = input(1712).split(' ');

const getBreakEventPoint = (fixedCost, variableCost, sellingCost) => {
  if(sellingCost - variableCost <= 0)
    return -1;
  const breakEvenPoint = Math.floor(fixedCost / (sellingCost - variableCost)) + 1;
  return breakEvenPoint;
}

console.log(getBreakEventPoint(+fixedCost, +variableCost, +sellingCost))