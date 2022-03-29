const { input } = require('../input');

const inputs = input(10250).split('\n');

const getResult = (height, width, number) => {
  let room = Math.ceil(number / height);
  let floor = number % height;
  return `${floor === 0 ? height : floor}${room.toString().padStart(2, '0')}`
}

const numOfTestCase = +inputs.shift();
for(let i = 0; i < numOfTestCase; i++){
  const [H, W, N] = inputs[i].split(' ');
  console.log(getResult(+H, +W, +N));
}