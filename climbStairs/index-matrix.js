/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  const M = [
    [1, 1],
    [1, 0],
  ];
  const result = power(M, n);
  return result[0][0];
};
// matrix multiply
const multiply = (a, b) => {
  const result = [
    [1, 0],
    [0, 1],
  ];
  result[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
  result[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1];
  result[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0];
  result[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1];
  // copy result to a?
  b[0][0] = result[0][0];
  b[0][1] = result[0][1];
  b[1][0] = result[1][0];
  b[1][1] = result[1][1];
};

//power
const power = (M, expo) => {
  let result = [
    [1, 0],
    [0, 1],
  ];
  while (expo > 0) {
    if (expo & 1) {
      multiply(M, result);
    }
    multiply(M, M);
    expo >>= 1;
  }
  return result;
};

const t = climbStairs(4);
