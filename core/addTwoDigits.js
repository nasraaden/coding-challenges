/* 
You are given a two-digit integer n. Return the sum of its digits.
*/
// function addTwoDigits(n) {
//   let number = n.toString().split("");
//   let sum = 0;
//   for (let i = 0; i < number.length; i++) {
//     sum += parseInt(number[i]);
//   }
//   return sum;
// }
function addTwoDigits(n) {
  return Math.floor(n / 10 + (n % 10));
}
