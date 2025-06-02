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
 * @return {boolean}
 */
var isValidBST = function (root) {
  const memo = {};
  // Memo is unnecessary, since we've checked order every node, it proves duplicated value to appear at the same position,
  // which is impossible
  // so only taking off equal mark works
  let min = -Infinity;
  let max = Infinity;
  let res = helper(memo, root, min, max);
  return res;
};
function helper(memo, root, min, max) {
  if (!root) return true;
  if (memo[root.val]) return false;
  memo[root.val] = 1;
  if (root.val < min || root.val > max) return false;

  //result of children
  let left, right;

  left = helper(memo, root.left, min, root.val);

  right = helper(memo, root.right, root.val, max);

  return left && right;
}
const t1 = {
  val: 5,
  left: {
    val: 1,
    right: null,
    left: null,
  },
  right: {
    val: 4,
    right: { val: 3, left: null, right: null },
    left: { val: 6, left: null, right: null },
  },
};
const t2 = {
  val: 2,
  left: { val: 2 },
  right: { val: 2 },
};
const t3 = {
  val: 2,
  left: { val: 1 },
  right: { val: 3 },
};
const t = isValidBST(t3);
