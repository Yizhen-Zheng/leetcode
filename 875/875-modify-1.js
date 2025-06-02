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
  if (piles.length === 1) {
    return Math.floor(piles[0] / h) + (piles[0] % h === 0 ? 0 : 1);
  }

  // pointers:
  let left = 0;
  let right = piles.length - 1;
  let mid = Math.floor((left + right) / 2);
  // result
  let k = piles[mid];

  while (left <= right) {
    // point to mid
    const time = eat(piles[mid], piles);

    // this case k is bigger or equal to slowest result, need to decrease k
    if (time <= h) {
      k = piles[mid];
      while (k > (piles[mid - 1] ?? 0)) {
        const T = eat(k, piles);
        // return k if find value on the edge
        if (T > h) {
          return k + 1;
        }
        k--;
      }
      k++;
      // if k are still enough, go left, descrease speed by update pointer
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
const t5 = [312884470]; //h=312884469
// const t = minEatingSpeed(t1, 6);
// const t = minEatingSpeed(t2, 8);
// const t = minEatingSpeed(t3, 3);
// const t = minEatingSpeed(t4, 3);
const t = minEatingSpeed(t5, 312884469);
