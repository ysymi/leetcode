#! coding=utf8
# ideas:
# 交换每一个节点的左右节点即可 写了个非递归版的 但是显然递归版的更精简:
# Solution(object):
#     def invertTree(self, root):
#         if(root == None): return
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root
# gains:
# 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        nodes = [root]
        while len(nodes) != 0:
            node = nodes.pop(0)
            if node:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

                node.left, node.right = node.right, node.left
        return root
