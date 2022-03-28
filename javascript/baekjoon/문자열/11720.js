
const { input } = require('../input.js');
const inputs = input(11720).split('\n');
const N = +inputs[0];
const numbers = inputs[1];
const sum = numbers.split('').reduce((acc, curr) => acc + +curr, 0);
console.log(sum);