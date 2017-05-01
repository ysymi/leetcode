#! coding=utf8
# ideas:
#
# gains:#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        cur_level, next_level = [root], []
        ret = []
        while len(cur_level) != 0:
            ret.append(max(node.val for node in cur_level))
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level, next_level = next_level, []

        return ret