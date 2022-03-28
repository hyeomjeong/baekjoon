const { input } = require('../input');

const str = input(2941).trim();

const replaceAll = (str, searchStr, replaceStr) => {
  return str.split(searchStr).join(replaceStr);
}

const convertCrotiaAlphabet2Space = (str) => {
  const CROTIA_ALPHABET = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='];
  for(let i = 0; i < CROTIA_ALPHABET.length; i++){
    str = replaceAll(str, CROTIA_ALPHABET[i], ' ');
  }
  return str;
}

const getCountOfAlphabet = (str) => {
  return convertCrotiaAlphabet2Space(str).length;
}

console.log(getCountOfAlphabet(str));