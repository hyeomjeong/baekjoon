const { input } = require('../input');

const number = +input(2839);

const getMinimum = (totalAmount) => {
  const BIG = 5;
  const SMALL = 3;
  let bigCount = Math.floor(totalAmount / BIG);
  while(bigCount >= 0){
    const bigNumber = totalAmount - (bigCount * BIG);
    if(bigNumber % SMALL === 0)
      return bigCount + (bigNumber / SMALL);
    bigCount--;
  }
  return -1;
}

console.log(getMinimum(number))