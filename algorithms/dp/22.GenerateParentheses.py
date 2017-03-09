class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = {1: set(['()'])}

        for i in range(2, n + 1):
            ret[i] = set()
            for s in ret[i - 1]:
                ret[i] |= set([s + '()', '()' + s, '(' + s + ')'])

        return sorted(list(ret[n]))
