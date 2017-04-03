# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        idx = 0
        while idx < len(nodes):
            if nodes[idx].left:
                nodes.append(nodes[idx].left)
            if nodes[idx].right:
                nodes.append(nodes[idx].right)
            idx += 1

        values = sorted([node.val for node in nodes])

        ret = values[1] - values[0]
        for i in xrange(2, idx):
            ret = min(ret, values[i] - values[i - 1])

        return ret
