const stdin = process.stdin;
stdin.resume();
stdin.setEncoding("utf8");

let input = "";
stdin.on("data", (chunk) => {
  input += chunk;
});
stdin.on("end", () => {
  const lines = input.trim().split("\n");
  const N = lines[0];
  const S = lines.slice(1, Number(N) + 1).map((s) => (s = s.split("")));

  const T = lines.slice(Number(N) + 1).map((s) => (s = s.split("")));

  const res = solve(N, S, T);
  process.stdout.write(res.toString());
});
// !!!!!!!!I forgot 0 degree!!!
function solve(N, S, T) {
  let res;
  for (let i = 0; i < 4; i++) {
    const count = rotateCompare(N, S, T, i);
    // console.log(res);
    res = res ? Math.min(res, count) : count;
    // console.log(res, "\n", "--------------");
  }
  return res;
}
function rotateCompare(N, S, T, i) {
  const A = (i.toString(2) >> 1) & 1;
  const B = i.toString(2) & 1;
  let count = i;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const origin = S[i][j];
      let target;
      if (!B && !A) {
        target = T[i][j];
      } else if (A && !B) {
        target = T[N - i - 1][N - j - 1];
      } else if (A && B) {
        target = T[N - j - 1][i];
      } else if (B && !A) {
        target = T[j][N - i - 1];
      }
      if (target !== origin) {
        count += 1;
      }
    }
  }

  return count;
}
