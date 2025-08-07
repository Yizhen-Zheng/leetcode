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
  function dfs(node) {
    visited.add(node);
    for (let neighbor of adjList[node]) {
      if (!visited.has(neighbor)) {
        dfs(neighbor);
      }
    }
  }
  dfs(1);

  return visited.size === N ? "Yes" : "No";
}
