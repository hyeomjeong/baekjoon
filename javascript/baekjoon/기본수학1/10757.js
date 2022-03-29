const { input } = require('../input');

const [A, B] = input(10757).split(' ').map(BigInt);

const addNumbers = (a, b) => a + b;

console.log(addNumbers(A, B).toString());