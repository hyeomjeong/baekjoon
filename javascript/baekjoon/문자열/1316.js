const { input } = require('../input');

const inputs = input(1316).split('\r\n');
const numOfWord = +inputs.shift();

const isGroupWord = (word) => {
  const a = 'a'.charCodeAt();
  const alphabet = new Array(26).fill(false);
  let prevAlphabet = word[0];
  for(let i = 0; i < word.length; i++){
    const currAlphabet = word[i];
    const currAlphabetIdx = currAlphabet.charCodeAt() - a;
    if(alphabet[currAlphabetIdx] && prevAlphabet !== currAlphabet)
      return false;
    alphabet[currAlphabetIdx] = true;
    prevAlphabet = currAlphabet;
  }
  return true;
}

const getNumOfGroupWord = (numOfWord, words) => {
  let numOfGroupWord = 0;
  for(let i = 0; i < numOfWord; i++){
    const word = words[i];
    if(isGroupWord(word))
      numOfGroupWord++;
  }
  return numOfGroupWord;
}

console.log(getNumOfGroupWord(numOfWord, inputs));