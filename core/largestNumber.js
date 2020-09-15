/*
Given an integer n, return the largest number that contains exactly n digits.
*/

function largestNumber(n) {
  // let num = ''
  // for(let i = 0; i<n; i++){
  //     num += '9'
  // }
  return 10 ** n - 1;
}
