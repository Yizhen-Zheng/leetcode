/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let resArr = s
    // .trim()
    .split(" ")
    .filter((str) => str !== "")
    .reverse()
    .join(" ");
  
  return resArr;
};