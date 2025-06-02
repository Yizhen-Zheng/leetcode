/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  // range: k: [1,fast]
  // edge: ASAP (k=fast)
  // pointers:
  let left = 1;
  let right = Math.max(...piles);
  let mid = Math.floor((left + right) / 2);
  // result
  let k = mid;

  while (left <= right) {
    // point to mid
    const time = eat(mid, piles);
    // this case k is bigger or equal to slowest result, need to decrease k
    if (time <= h) {
      k = mid;
      // since k is still enough, go left, descrease speed by update pointer
      right = mid - 1;
      mid = Math.floor((left + right) / 2);
    } else {
      // go right, increase speed
      left = mid + 1;
      // update mid for next loop
      mid = Math.floor((left + right) / 2);
    }
  }
  return k;
};

const eat = (k, piles) => {
  // count hours needed
  let count = 0;
  for (let p of piles) {
    count += Math.ceil(p / k);
  }
  return count;
};
const t1 = [30, 11, 23, 4, 20]; //h = 6
const t2 = [3, 6, 7, 11]; //h = 8
const t3 = [1000000000, 1000000000]; //h = 3
const t4 = [2, 2, 2]; //h = 3 exp: 2
const t5 = [312884470]; //h=312884469
// const t = minEatingSpeed(t1, 6);
// const t = minEatingSpeed(t2, 8);
// const t = minEatingSpeed(t3, 3);
// const t = minEatingSpeed(t4, 3);
const t = minEatingSpeed(t5, 312884469);
