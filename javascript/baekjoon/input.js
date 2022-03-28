const fs = require('fs');
const path = require('path');

const input = function(questionNumber) {
  const inputPath = process.platform === 'linux' ? '/dev/stdin' : `${__dirname}/inputs/${questionNumber}.txt`;
  return fs.readFileSync(inputPath).toString();
}

module.exports = {
  input
}