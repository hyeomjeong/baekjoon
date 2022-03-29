const { input } = require('../input');

const number = +input(1193);

const getFraction = (number) => {
  const DIRECTION = {
    UP: [-1, 1],
    DOWN: [1, -1]
  }
  let direction = 'UP';
  let count = 1;
  let row = 1;
  let col = 1;
  while(count < number){
    if(row === 1 && direction === 'UP'){
      col++;
      direction = 'DOWN';
    }
    else if(col === 1 && direction === 'DOWN'){
      row++;
      direction = 'UP' ;
    }
    else{
      const [r, c] = DIRECTION[direction];
      row += r;
      col += c;
    }
    count++;
  }
  return `${row}/${col}`
}

console.log(getFraction(number))