const { input } = require('../input');

const inputs = input(2675).split('\r\n');
const numOfTestCase = +inputs.shift();
const repeatStr = (numOfRepetition, str) => {
  let result = '';
  for(let i = 0; i < str.length; i++){
    result += str[i].repeat(numOfRepetition);
  }
  return result;
}

const result = [];
for(let i = 0; i < numOfTestCase; i++){
  const [numOfRepetition, str] = inputs[i].split(' ');
  result.push(repeatStr(numOfRepetition, str));
}

console.log(result.join('\n'));