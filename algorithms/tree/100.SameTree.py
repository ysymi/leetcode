# coding=utf8
#  ideas:
# bfs遍历转化为可比较的对象，再比较结构和值
#
# gains:
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def parse_tree(root):
            if root is None:
                return []

            nodes = [root]
            idx = 0
            while idx < len(nodes):
                if nodes[idx]:
                    nodes.append(nodes[idx].left)
                    nodes.append(nodes[idx].right)
                idx += 1
            return nodes

        p = parse_tree(p)
        q = parse_tree(q)

        if len(p) != len(q):
            return False

        for i in range(len(p)):
            if q[i] is None and p[i] is None:
                continue
            if q[i] and p[i] and q[i].val == p[i].val:
                continue
            return False

        return True
