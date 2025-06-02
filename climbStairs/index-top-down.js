/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let memo = new Array(n + 1);
  //not array(n)!
  //   we use this for convenient to get index, so we don't need memo[n-1] every time
  memo.fill(-1, 0);
  console.log(memo);
  const result = helper(n, memo);
  return result;
};

function helper(n, memo) {
  if (n <= 1) return 1;
  if (memo[n] !== -1) return memo[n];
  memo[n] = helper(n - 1, memo) + helper(n - 2, memo);
  return memo[n];
}
const r = climbStairs(5);
console.log(r);
