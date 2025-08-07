const stdin = process.stdin;
stdin.resume();
stdin.setEncoding("utf8");

let input = "";
stdin.on("data", (chunk) => {
  input += chunk;
});

stdin.on("end", () => {
  //   console.log(input);
  const lines = input.trim().split("\n");
  // Process input here
  const res = solve(lines[0]);
  process.stdout.write(res);
  process.exit();
});

function solve(str) {
  //
  const map = new Array(26).fill(0);
  for (let i = 0; i < str.length; i++) {
    map[str.charCodeAt(i) - 97] = 1;
  }

  const res = String.fromCharCode([97 + map.indexOf(0)]);

  return res;
}
//
