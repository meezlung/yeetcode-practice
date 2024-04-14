# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def recurse(node):
            if node == None:
                return 0

            add = 0 

            if node.left and (node.left.left == None and node.right.right == None): 
                # if the left and right node of this current left node is none, then it is a left leaf node
                # if a left leaf node, add to the sum

                add += node.left.val         

            return add + recurse(node.left) + recurse(node.right)

        return recurse(root)