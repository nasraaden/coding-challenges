/*
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.
*/

var findDuplicates = function (nums) {
  let obj = {};
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    if (obj[nums[i]]) {
      result.push(nums[i]);
    } else {
      obj[nums[i]] = 1;
    }
  }
  return result;
};
