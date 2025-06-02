/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function (word1, word2) {
  if (word1.length !== word2.length) {
    return false;
  }
  const map1 = new Array(26).fill(0);
  const map2 = new Array(26).fill(0);
  for (let i = 0; i < word1.length; i++) {
    if (!word2.includes(word1[i])) return false;
    map1[word1[i].charCodeAt(0) - 97] += 1;
    map2[word2[i].charCodeAt(0) - 97] += 1;
  }

  const arr1 = JSON.stringify(map1.sort((a, b) => a - b));
  const arr2 = JSON.stringify(map2.sort((a, b) => a - b));

  return arr1 === arr2;
};
const t1 = { 1: "cabbba", 2: "abbccb" };
const t2 = { 1: "uau", 2: "ssx" };
const t = closeStrings(t1[1], t1[2]);
// const t = closeStrings(t2[1], t2[2]);
