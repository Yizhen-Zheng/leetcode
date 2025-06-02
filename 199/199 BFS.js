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

// breadth first search, layer
var rightSideView = function (root) {
  if (!root) {
    return [];
  }
  let result = [];
  let idx = 0;
  let queue = [root];
  while (idx < queue.length) {
    // let currentRow = [];
    const width = queue.length - idx;
    for (let i = 0; i < width; i++) {
      // update idx
      const node = queue[idx++];
      // only push to current row if not null
      if (node !== null && node.val !== null) {
        // currentRow.push(node.val);
        if (node.left !== null) {
          queue.push(node.left);
        }
        if (node.right !== null) {
          queue.push(node.right);
        }
      }
    }
    result.push(queue[idx - 1].val);
  }
  return result;
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
const t2 = {};
const t3 = {
  val: 1,
  left: {
    val: 2,
    right: { val: 5, left: null, right: null },
    left: null,
  },
  right: { val: 3, right: { val: 4, left: null, right: null }, left: null },
};
const t = rightSideView(t1);
console.log(t);
