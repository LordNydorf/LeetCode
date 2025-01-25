# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def walk(root):
            if root:
                yield from walk(root.right)
                yield root.val
                yield from walk(root.left)
        return min(starmap(operator.sub, pairwise(walk(root))))
