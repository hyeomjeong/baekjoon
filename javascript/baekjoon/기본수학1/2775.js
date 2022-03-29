const { input } = require('../input');

const inputs = input(2775).split('\r\n');

const getNumOfResidents = (floor, roomNumber) => {
  let prevFloor = new Array(roomNumber).fill(0).map((_, idx) => idx + 1);
  for(let i = 0; i < floor; i++){
    const currFloor = [prevFloor[0]];
    for(let i = 1; i < roomNumber; i++){
      const numOfResidents = prevFloor[i] + currFloor[i-1];
      currFloor.push(numOfResidents);
    }
    prevFloor = currFloor;
  }
  return prevFloor.pop();
}

const numOfTestCase = +inputs.shift();
for(let i = 0; i < numOfTestCase; i++){
  const k = +inputs.shift();
  const n = +inputs.shift();
  console.log(getNumOfResidents(k, n));
}