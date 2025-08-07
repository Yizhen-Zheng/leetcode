const stdin = process.stdin;
stdin.resume();
stdin.setEncoding("utf8");

let input = "";
stdin.on("data", (chunk) => {
  input += chunk;
});
stdin.on("end", () => {
  const lines = input.trim().split("\n");
  const N = parseInt(lines[0]);
  const S = lines.slice(1, N + 1).map((s) => (s = s.split("")));
  const T = lines.slice(N + 1).map((s) => (s = s.split("")));
  const res = solve(N, S, T);
  process.stdout.write(res.toString());
});
function solve(N, S, T) {
  let res = Infinity;
  for (let i = 0; i < 4; i++) {
    const count = rotateCompare(N, S, T, i) + i;

    res = Math.min(res, count);
  }
  return res;
}
function rotateCompare(N, S, T, r) {
  let count = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      const origin = S[i][j];
      let target;
      if (r === 0) {
        target = T[i][j];
      } else if (r === 1) {
        target = T[j][N - i - 1];
      } else if (r === 2) {
        target = T[N - i - 1][N - j - 1];
      } else if (r === 3) {
        target = T[N - j - 1][i];
      }

      if (target !== origin) {
        count += 1;
      }
    }
  }
  return count;
}
