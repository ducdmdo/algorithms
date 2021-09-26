# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        #base case
        if root is None:
            return None
        #recurrence relation
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root
        print(root)
        print(val)




node1 = TreeNode(1, None, None)
node3 = TreeNode(3, None, None)
node2 = TreeNode(2, node1, node3)
node7 = TreeNode(7, None, None)
bst_root = TreeNode(4,node2, node7)

solution = Solution()
print (solution.searchBST(bst_root,2))
