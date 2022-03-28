const {input} = require('../input');

const A = 'A'.charCodeAt();
const word = input(1157).toUpperCase();

const getCountOfAlphabet = (word) => {
  const alphabet = new Array(26).fill(0);
  for(let i = 0; i < word.length; i++){
    alphabet[word[i].charCodeAt() - A]++;
  }
  return alphabet;
}

const getMaximumAlphabet = (alphabet) => {
  const maximumCount = Math.max(...alphabet);
  const index = alphabet.indexOf(maximumCount);
  if(index !== alphabet.lastIndexOf(maximumCount))
    return '?';
  return String.fromCharCode(index + A);
}


console.log(getMaximumAlphabet(getCountOfAlphabet(word)));