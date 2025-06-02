/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let start = 0;
  let end = 0;
  let len = s.length;
  let arr = [];
  while (start < len && end < len) {
    while (s[start] === " ") {
      start++;
    }
    end = start;
    while (s[end] && s[end] !== " ") {
      end++;
    }
    if (start !== end) {
      arr.push(s.substring(start, end));
    }
    start = end;
  }
  return arr.reverse().join(" ");
};
const s = "  hello world  ";
const s2 = "a good   example";
const s3 = "the sky is blue";
const t = reverseWords(s);
