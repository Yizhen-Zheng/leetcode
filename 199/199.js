/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
//---------------------- THIS NOT WORK(PARTLY) ----------------------
// breadth first search
var rightSideView = function (root) {
  if (!root) {
    return [];
  }
  const rootArr = traverse(root);
  let result = [];
  let idx = 0;
  let currentRow = 0;
  //   next step's current row's right end

  //   next step's current row's left end
  let leftMost = 0;
  //   go right child: 2*n+2
  // horizontally move left: n-1

  while (leftMost < rootArr.length) {
    //
    if (rootArr[idx]) {
      result.push(rootArr[idx]);
      //   go right leaf
      idx = idx * 2 + 2;
      let width = 2 ** currentRow;
      leftMost += width;
      currentRow++;
      //   rightMost += 2 * width;
    } else {
      // if right is null
      if (!rootArr[idx] && idx > leftMost) {
        idx--;
      } else if (rootArr[idx] === null && idx == leftMost) {
        break;
      }
    }
  }
  return result;
};
const traverse = (root) => {
  // traverse tree with place holder null
  const arr = [];
  const queue = [root];
  let idx = 0;
  while (queue.length > idx) {
    const node = queue[idx];
    arr.push(node === null ? null : node.val);
    if (node !== null) {
      queue.push(node.left === null ? null : node.left);
      queue.push(node.right === null ? null : node.right);
    }
    idx++;
  }
  return arr;
};
const t1 = {
  val: 6,
  left: {
    val: 1,
    right: {
      val: 3,
      left: { val: 2, left: null, right: null },
      right: { val: 5, left: { val: 4, left: null, right: null }, right: null },
    },
    left: null,
  },
  right: null,
};
const t2 = [];
const t3 = [1, 2, 3, null, 5, null, 4];
const t = rightSideView(t1);
console.log(t);
