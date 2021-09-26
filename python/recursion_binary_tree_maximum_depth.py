# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Base case
        if root is None:
            result = 0
        else:
            result = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return result

solution = Solution()
solution.maxDepth()
