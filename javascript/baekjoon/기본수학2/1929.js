const { input } = require('../input');

const [M, N] = input(1929).split(' ');

const isPrime = (number) => {
  if(number === 1)
    return false;
  for(let i = 2; i*i <= number; i++){
    if(number % i === 0)
      return false;
  }
  return true;
}

const getPrimes = (smallNumber, bigNumber) => {
  const primes = [];
  for(let i = smallNumber; i <= bigNumber; i++){
    if(isPrime(i))
      primes.push(i);
  }
  return primes;
}

const solution = (smallNumber, bigNumber) => {
  const primes = getPrimes(smallNumber, bigNumber);
  console.log(primes.join('\n'));
}

solution(+M, +N);