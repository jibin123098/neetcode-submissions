# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result=[0]
        def findheight(node):
            if node is None:
                return 0
            left=findheight(node.left)
            right=findheight(node.right)
            current_diameter=left+right
            if current_diameter>result[0]:
                result[0]=current_diameter
            return 1+max(left,right)

        findheight(root)
        return result[0]