/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
  let left = 1,
    right = Infinity,
    ans = null,
    prevLeft = null;
  while (left <= right) {
    const divisor = right === Infinity ? left : Math.floor((left + right) / 2);
    const eatTimeOut = eat(piles, divisor, limit);
    if (eatTimeOut) {
      prevLeft = left;
      left = right === Infinity ? left * 2 : divisor + 1;
    } else {
      ans = divisor;
      right = ans - 1;
      left = prevLeft + 1;
    }
  }
  return ans;
};

const eat = (nums, divisor, limit) => {
  let sum = 0;
  for (const num of nums) {
    sum += Math.ceil(num / divisor);
    if (sum > limit) return true;
  }
  return false;
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
