const { input } = require('../input');

const [A, B, V] = input(2869).split(' ');

const getTimeToClimb = (day, night, height) => {
  return Math.ceil((height - night) / (day - night));
}

console.log(getTimeToClimb(+A, +B, +V));