const { input } = require('../input');

const [numberA, numberB] = input(2908).split(' ');

const reverseNumber = (number) => {
  let reveredNumber = '';
  for(let i = number.length-1; i >= 0; i--)
    reveredNumber += number[i];
  return +reveredNumber;
}

const findBiggerNumber = (a, b) => {
  return Math.max(reverseNumber(a), reverseNumber(b));
}

console.log(findBiggerNumber(numberA, numberB));