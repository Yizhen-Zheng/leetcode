/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  function check(piles, h, mid) {
    let ans = 0;
    for (let pile of piles) {
      ans += Math.ceil(pile / mid);
    }
    return ans <= h;
  }
  let low = 1;
  let high = Math.max(...piles);
  while (low < high) {
    let mid = Math.floor((low + high) / 2);
    if (check(piles, h, mid)) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }
  return low;
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
