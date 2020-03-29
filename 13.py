#coding:utf-8
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root: return []

        def helper(root, sum, tmp):
            if not root:
                return
            if not root.left and not root.right and sum - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
                return
            helper(root.left, sum - root.val, tmp + [root.val])
            helper(root.right, sum - root.val, tmp + [root.val])

        helper(root, sum, [])
        return res



if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    sum = 22
    a = solution.pathSum(root, sum)
    print(a)