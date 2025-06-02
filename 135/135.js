/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function (ratings) {
  let currentIdx;
  //  store candy number
  let lookUp = {};
  const queue = [0];
  while (queue.length) {
    currentIdx = queue[queue.length - 1];
    const current = arr[currentIdx];
    const prev = arr[current - 1];
    const next = arr[current + 1];
  }
  if (current > (prev ?? -1) || current > (next ?? -1)) {
    if (current > (prev ?? -1) && current > (next ?? -1)) {
      // greater than both
    } else if (prev ?? -1 > next ?? -1) {
      //prev > current > next
    } else {
      // next > current > next
    }
  } else {
    if (lookUp[idx]) {
      queue.pop();
    } else {
      lookUp[idx] = 1;
      queue.push(idx + 1);
    }
  }
  return Object.entries(lookUp).reduce((innerArr, acc) => innerArr[1] + acc);
  // if greater than neighbour: prev+1
  // --------------maybe Recursive to the lowest point? (1) or whatever--------------
  // or 2 pointer to find the entry point?
};
function helper(arr, idx, lookUp) {
  const prev = arr[idx - 1];
  const next = arr[idx + 1];
  const current = arr[idx];
  // greater than at least one neighbor
  if (current > (prev ?? -1) || current > (next ?? -1)) {
    if (current > (prev ?? -1) && current > (next ?? -1)) {
      // greater than both
    } else if (prev ?? -1 > next ?? -1) {
      //prev > current > next
    } else {
      // next > current > next
    }
  } else {
    lookUp[idx] = 1;
  }
}
const t1 = [1, 2, 2];
const t = candy(t1);
