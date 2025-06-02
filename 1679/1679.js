/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
// Array.sort(): T(O):(n logn)
var maxOperations = function (nums, k) {
  nums.sort((a, b) => a - b);
  let left = 0;
  let right = nums.length - 1;
  let count = 0;
  while (nums[left] < k && left < right) {
    const sum = nums[left] + nums[right];
    if (sum === k) {
      left++;
      right--;
      count++;
    } else if (sum < k) {
      left++;
    } else if (sum > k) {
      right--;
    }
  }
  return count;
};
const t1 = [3, 1, 3, 4, 3];
const t2 = [1, 2, 3, 4];
const t = maxOperations(t1, 6);
