# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        max_depth = 0
        curr = root
        while curr.left is not None:
            max_depth += 1
            curr = curr.left        
        lo, hi = 0, (1 << max_depth) - 1

        def check_leaf(a, d):
            curr = root
            for i in range(d-1, -1, -1):
                if a & (1 << i):
                    curr = curr.right
                else:
                    curr = curr.left
            return curr is not None        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check_leaf(mid, max_depth):
                lo = mid
            else:
                hi = mid - 1
        return ((1 << max_depth) - 1) + lo + 1      
