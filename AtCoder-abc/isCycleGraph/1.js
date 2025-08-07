const stdin = process.stdin;
stdin.resume();
stdin.setEncoding("utf8");

let input = "";
stdin.on("data", (chunk) => {
  input += chunk;
});
stdin.on("end", () => {
  const lines = input.trim().split("\n");
  // console.log(lines);
  const [N, M] = lines[0].split(" ").map((s) => parseInt(s));
  const nodes = lines.slice(1).map((s) => s.split(" ").map((s) => parseInt(s)));
  const res = solve(N, M, nodes);
  process.stdout.write(res.toString());
});

function solve(N, M, nodes) {
  //

  if (N !== M) return "No";
  const adjList = {};
  for (let i = 1; i <= N; i++) {
    adjList[i] = [];
  }
  for (let pair of nodes) {
    adjList[pair[0]].push(pair[1]);
    adjList[pair[1]].push(pair[0]);
  }
  // console.log(adjList);
  for (let i = 1; i <= N; i++) {
    if (adjList[i].length !== 2) {
      return "No";
    }
  }
  // basic check finish

  const visited = new Set();

  let current = 1;
  let prev = -1;
  for (let i = 0; i < N; i++) {
    visited.add(current);
    let next = -1;
    for (let neighbor of adjList[current]) {
      if (neighbor !== prev) {
        next = neighbor;
        break;
      }
    }
    if (i === N - 1) {
      return next === 1 ? "Yes" : "No";
    }
    prev = current;
    current = next;
  }
  return "No";
}
function dfs(adjList, node, visited, N) {
  visited.add(node);
  const [a, b] = adjList[node];
  console.log(a, b);
  if (visited.size === N && (a === 1 || b === 1)) {
    return true;
  }
  if (!visited.has(a)) {
    return dfs(adjList, a, visited, N);
  } else {
    return dfs(adjList, b, visited, N);
  }
}
