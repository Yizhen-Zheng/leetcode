// /**
//  * @param {number} n
//  * @return {number}
//  */
// var climbStairs = function (n) {
//   let tabu = [1, 1];
//   console.log(tabu);
//   for (let i = 0; i < n + 1; i++) {
//     if (!tabu[i]) {
//       tabu[i] = tabu[i - 1] + tabu[i - 2];
//     }
//   }
//   return tabu[n];
// };
// const t = climbStairs(4);

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let tabu = [1, 1];
  // better use 2 let , not an arr
  for (let i = 2; i < n + 1; i++) {
    let temp = tabu[0] + tabu[1];
    tabu = [tabu[1], temp];
  }
  return tabu[1];
};
const t = climbStairs(4);
