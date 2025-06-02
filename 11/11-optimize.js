/**
 * @param {number[]} height
 * @return {number}
 */
// 2 loop
var maxArea = function (height) {
  let result = 0;
  // pointers
  let leftPointer = 0;
  let rightPointer = height.length - 1;

  while (rightPointer > leftPointer) {
    let len = rightPointer - leftPointer;
    const vol = Math.min(height[rightPointer], height[leftPointer]) * len;
    if (vol > result) {
      result = vol;
    }
    if (height[rightPointer] <= height[leftPointer]) {
      rightPointer--;
    } else {
      leftPointer++;
    }
    // if current left - current right
  }
  return result;
};
// height*height*dist
const t1 = [1, 1];
const t2 = [1, 8, 6, 2, 5, 4, 8, 3, 7];
const t3 = [8, 7, 2, 1];
const t = maxArea(t3);
