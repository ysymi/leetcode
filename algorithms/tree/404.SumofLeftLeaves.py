# coding=utf8
# ideas:
# 看清题目 要的是左叶子
#
# gains:
# x for x in xxx 就是一个 generator

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        root.is_left = False
        root.is_leaves = True

        nodes = [root]
        idx = 0
        while idx < len(nodes):
            nodes[idx].is_leaves = True
            if nodes[idx].left:
                nodes[idx].is_leaves = False
                nodes[idx].left.is_left = True
                nodes.append(nodes[idx].left)
            if nodes[idx].right:
                nodes[idx].is_leaves = False
                nodes[idx].right.is_left = False
                nodes.append(nodes[idx].right)
            idx += 1

        return sum(node.val for node in nodes if node.is_left and node.is_leaves)
