/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  let idx = 0;
  const arr = [];
  let buffer = "";
  while (s[idx]) {
    let char = s[idx];
    if (char === " " && buffer.length > 0) {
      arr.push(buffer);
      buffer = "";
    } else if (char !== " ") {
      buffer += char;
    }
    idx++;
  }
  if (buffer.length > 0) {
    arr.push(buffer);
    buffer = "";
  }
  //   2 pointers
  for (let i = arr.length - 1; i > 0; i--) {
    buffer += arr[i];
    buffer += " ";
  }
  return buffer + arr[0];
};
const s = "  hello world  ";
const s2 = "a good   example";
const s3 = "the sky is blue";
const t = reverseWords(s);
