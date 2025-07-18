/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
// T(O): (n^2)
// S(O): (n)
var maxVowels = function (s, k) {
  let maxNum = 0;
  const len = s.length;
  let idx = 0;
  let memo = 0;
  while (idx < len) {
    if (idx >= k) {
      // update memo by one shift
      if (checkVowels(s[idx - k])) {
        memo -= 1;
      }
      if (checkVowels(s[idx])) {
        memo += 1;
      }
      //   conditional update maxNum
      maxNum = maxNum > memo ? maxNum : memo;
    } else {
      // coefficient: idx<k
      if (checkVowels(s[idx])) {
        maxNum++;
      }
      //   update this initial value to memo
      memo = maxNum;
    }
    idx++;
  }
  // substring
  // compare
  // update
  return maxNum;
};
const checkVowels = (char) => {
  return (
    char === "a" || char === "e" || char === "i" || char === "o" || char === "u"
  );
};
const t1 = "abciiidef";
const t2 = "leetcode";
const t = maxVowels(t2, 3);
