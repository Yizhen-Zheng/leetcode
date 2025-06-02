/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  piles.sort((a, b) => a - b);
  // range: k: [1,piles[piles.length - 1]]
  // edge: ASAP
  const last = piles[piles.length - 1];
  if (piles.length === h) {
    return last;
  }
  // edge: slowest
  if (h >= piles.reduce((a, b) => a + b)) {
    return 1;
  }

  // a not exits array from 1 to asap

  let left = 1;
  let right = last;
  let mid = Math.floor((left + right) / 2);
  let k = mid;
  // maybe 2 kinds of BST,
  // one is to search piles itself, and decrease until smallest
  // or search all speed (1, last)
  while (left <= right) {
    // point to mid
    const time = eat(mid, piles);
    // this case k is bigger or equal to slowest result, need to decrease k
    if (time <= h) {
      // go left, descrease speed
      right = mid - 1;
      // update pointer
      k = mid;
      // update mid for next loop
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
    count += Math.floor(p / k);
    if (p % k > 0) {
      count++;
    }
  }
  return count;
};
const t1 = [30, 11, 23, 4, 20]; //h = 6
const t2 = [3, 6, 7, 11]; //h = 8
const t3 = [1000000000, 1000000000]; //h = 3
const t4 = [2, 2, 2]; //h = 3 exp: 2
// const t = minEatingSpeed(t4, 3);
const t = minEatingSpeed(t3, 3);
// const t = minEatingSpeed(t1, 6);
// const t = minEatingSpeed(t2, 8);
