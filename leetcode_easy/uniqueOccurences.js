/*
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
*/
var uniqueOccurrences = function (arr) {
  let obj = {};
  for (let i = 0; i < arr.length; i++) {
    if (!obj[arr[i]]) {
      obj[arr[i]] = 1;
    }
    obj[arr[i]]++;
  }
  let values = Object.values(obj);
  return new Set(Object.values(obj)).size === values.length;
};
