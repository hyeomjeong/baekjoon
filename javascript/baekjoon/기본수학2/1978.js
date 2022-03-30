const { input } = require('../input');

const inputs = input(1978).split('\r\n');
const N = +inputs.shift();
const numbers = inputs[0].split(' ');

const isPrime = (number) => {
  if(number === 1)
    return false;
  for(let i = 2; i*i <= number; i++){
    if(number % i === 0) 
      return false;
  }
  return true;
}

const getNumOfPrime = (numbers) => {
  let count = 0;
  numbers.forEach((number) => {
    if(isPrime(+number)){
      count++;
    }
  })
  return count;
}

console.log(getNumOfPrime(numbers));