#! coding=utf8
# ideas:
#
# gains:
#


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []

        def dfs(node):
            if node:
                dfs(node.left)
                ret.append(node.val)
                dfs(node.right)

        dfs(root)
        return ret
