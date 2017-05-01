#! coding=utf8
# ideas:
# 每次从左往右取一层的节点，取第一个值
# gains:#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_level, next_level = [root], []
        ret = root.val
        while len(cur_level) != 0:
            ret = cur_level[0].val
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level, next_level = next_level, []

        return ret


