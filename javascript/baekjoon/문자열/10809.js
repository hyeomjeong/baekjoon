const { input } = require('../input.js');

const word = input(10809);
const A_ASCII_CODE = 97;

const alphabet = new Array(26).fill(-1);

for(let i = 0; i < word.length; i++){
  const currAlphabetIndex = word[i].charCodeAt() - A_ASCII_CODE;
  if(alphabet[currAlphabetIndex] !== -1)
    continue;
  alphabet[currAlphabetIndex] = i;
}

console.log(alphabet.join(' '));