const { input } = require('../input');

const words = input(1152).trim().split(' ');
const getNumOfWord = (words) => {
  let countOfWord = 0;
  for(let i = 0; i < words.length; i++){
      if(words[i] === '')
          continue;
      countOfWord++;
  }
  return countOfWord;
}
console.log(getNumOfWord(words));