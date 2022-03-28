const { input } = require('../input');

const phoneNumber = input(5622).trim();
const BASIC_TIME = 1;
const GROUP_OF_CODE = {
  2: ['A','B','C'],
  3: ['D', 'E', 'F'], 
  4: ['G', 'H', 'I'],
  5: ['J', 'K', 'L'],
  6: ['M', 'N', 'O'],
  7: ['P', 'Q', 'R', 'S'],
  8: ['T', 'U', 'V'],
  9: ['W', 'X', 'Y', 'Z']
}
const getRequireTime = (alphabet) => {
  for(let i = 2; i < 10; i++){
    const codes = GROUP_OF_CODE[i];
    if(!codes.includes(alphabet))
      continue;
    return i + BASIC_TIME;
  }
}

const getTotalTime = (word) => {
  let totalTime = 0;
  for(let i = 0; i < word.length; i++){
    totalTime += getRequireTime(word[i]);
  }
  return totalTime;
}

console.log(getTotalTime(phoneNumber));