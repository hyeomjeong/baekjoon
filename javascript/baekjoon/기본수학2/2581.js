const { input } = require('../input');

const [M, N] = input(2581).split('\r\n');

const isPrime = (number) => {
  if(number === 1)
    return false;
  for(let i = 2; i*i <= number; i++){
    if(number % i === 0)
      return false;
  }
  return true;
}

const solution = (smallNumber, bigNumber) => {
  let minimumOfPrimes = -1;
  let sumOfPrimes = 0;
  for(let i = smallNumber; i <= bigNumber; i++){
    if(!isPrime(i))
      continue;
    sumOfPrimes += i;
    if(minimumOfPrimes === -1)
      minimumOfPrimes = i;
  }
  return sumOfPrimes > 0 ? `${sumOfPrimes}\n${minimumOfPrimes}` : -1;
}

console.log(solution(+M, +N));