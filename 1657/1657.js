/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function (word1, word2) {
  if (word1.length !== word2.length) {
    return false;
  }
  const map1 = {};
  const map2 = {};
  for (let i = 0; i < word1.length; i++) {
    if (!word2.includes(word1[i])) return false;
    map1[word1[i]] = (map1[word1[i]] ?? 0) + 1;
    map2[word2[i]] = (map2[word2[i]] ?? 0) + 1;
  }

  console.log(map1, map2);
  console.log(Object.values(map1));
  const arr1 = JSON.stringify(Object.values(map1).sort());
  const arr2 = JSON.stringify(Object.values(map2).sort());

  return arr1 === arr2;
};
const t1 = { 1: "cabbba", 2: "abbccb" };
const t2 = { 1: "uau", 2: "ssx" };
const t = closeStrings(t2[1], t2[2]);
