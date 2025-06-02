/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  // trim is optional, but seems adding trim makes it run faster
  let resArr = s
    .trim()
    .split(" ")
    .filter((str) => str !== "")
    .reverse()
    .join(" ");
  // when split space by space, it returns number of space + 1 ''s
  // e.g.: '   '.split() 3 spaces, returns '','','',''
  // coefficient as 'a a a a'
  let example = "      ".split(" ");
  console.log(example);
  return resArr;
};
const s = "  hello world  ";
const s2 = "a good   example";
const s3 = "the sky is blue";
const t = reverseWords(s2);
