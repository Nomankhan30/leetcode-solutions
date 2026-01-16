from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #stopping criteria/base case
        if root is None:
            return 0

        # recursive case
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
