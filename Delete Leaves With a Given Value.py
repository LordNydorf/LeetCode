# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, r: Optional[TreeNode], t: int) -> Optional[TreeNode]:
        def f(n):
            if n:
                n.left, n.right = f(n.left), f(n.right)
                if n.left == n.right == None and n.val == t:
                    return None
                else:
                    return n
        return f(r)
