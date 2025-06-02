/**
 * @param {number[]} height
 * @return {number}
 */
// 2 loop
var maxArea = function (height) {
  let left = 0;
  let right = 0;
  for (let i = 0; i < height.length; i++) {
    for (let j = i; j < height.length; j++) {
      if (
        j - i > right - left &&
        Math.min(height[j], height[i]) >= Math.min(height[left], height[right])
      ) {
        left = i;
        right = j;
      }
    }
  }
  return Math.min(height[left], height[right]) * (right - left);
};
// height*height*dist
const t1 = [1, 1];
const t2 = [1, 8, 6, 2, 5, 4, 8, 3, 7];
const t = maxArea(t2);
