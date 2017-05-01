#! coding=utf8
# ideas:
# 题意：有几层就是几。 按层次遍历
# gains:
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cur_level, next_level = [root], []
        ret = 0
        while len(cur_level) != 0:
            ret += 1
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            cur_level, next_level = next_level, []

        return ret