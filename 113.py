class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        def backtrack(sum, root, pt):
            sum -= root.val
            pt.append(root.val)
            if not root.left and not root.right:
                if sum == 0:
                    self.ans.append(pt[:])
                    pt.pop()
                    return
                else:
                    pt.pop()
                    return
            elif not root.left and root.right:
                backtrack(sum, root.right, pt)
                pt.pop()
            elif root.left and not root.right:
                backtrack(sum, root.left, pt)
                pt.pop()
            else:
                backtrack(sum, root.left, pt)
                backtrack(sum, root.right, pt)
                pt.pop()
        self.ans = []
        if not root:
            return []
        backtrack(sum, root, [])
        return self.ans


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