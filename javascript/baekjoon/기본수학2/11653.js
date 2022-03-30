const { input } = require('../input');

const N = +input(11653);

const primeFactorization = (number) => {
  const result = [];
  let p = 2
  while(number !== 1){
    if (number % p === 0){
      number /= p;
      result.push(p);
    }
    else
      p++;
  }
  return result;
}

const solution = (number) => {
  const result = primeFactorization(number);
  if(result.length > 0)
    console.log(result.join('\n'));
}

solution(N);