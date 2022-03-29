const { input } = require('../input');

const number = +input(2292);

const getCountOfRoom = (number) => {
  let prevNumber = 1;
  for(let i = 1; i; i++){
    const currNumber = prevNumber + (6 * (i-1));
    if(currNumber >= number)
      return i;
    prevNumber = currNumber;
  }
}

console.log(getCountOfRoom(number))