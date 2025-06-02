/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function (nums, k) {
  let idx = 0;
  let map = {};
  let count = 0;
  while (idx < nums.length) {
    if (nums[idx] <= k) {
      const pair = k - nums[idx];
      if (map[pair]) {
        count++;
        if (map[pair] > 1) {
          map[pair]--;
        } else {
          map[pair] = null;
        }
      } else {
        if (map[nums[idx]]) {
          map[nums[idx]]++;
        } else {
          map[nums[idx]] = 1;
        }
      }
    }
    idx++;
  }
  return count;
};
const t1 = [3, 1, 3, 4, 3];
const t2 = [1, 2, 3, 4];
const t3 = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2];
const t4 = [2, 1, 3, 1, 1, 2, 1, 2, 2, 3, 2, 2];
const t = maxOperations(t3, 3);
