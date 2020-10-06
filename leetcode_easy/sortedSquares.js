/*
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
*/

function sortedSquares(arr) {
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i] ** 2;
  }
  let sorted = arr.sort(function (a, b) {
    return a - b;
  });
  return sorted;
}
