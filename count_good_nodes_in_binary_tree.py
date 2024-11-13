# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        maxim = root.val
        def dfs(node, maxi, path):
            if not node:
                return 0
            path.append(node.val)
            if node.val >= maxi:
                maxi = node.val
                currGood = 1
            #print(path)
            leftGood = dfs(node.left, maxi, path)
            rightGood = dfs(node.right, maxi, path)
            currGood = node.val >= maxi
            path.pop()
            return leftGood + rightGood + currGood
        result = dfs(root, maxim, path)
        print(path)
        return result
        