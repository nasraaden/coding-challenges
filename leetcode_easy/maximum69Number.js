/*
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
*/

function maximum69Number(num) {
  let stringNums = num.toString();
  let arrNums = stringNums.split("");
  console.log(arrNums);
  for (let i = 0; i < arrNums.length; i++) {
    if (arrNums[i] === "6") {
      arrNums[i] = "9";
      break;
    }
  }
  return arrNums.join("");
}
