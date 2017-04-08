# coding=utf8
# ideas:
#
#
# gains:
#


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ret = 0
        while x or y:
            ret += x & 1 != y & 1
            x >>= 1
            y >>= 1
        return ret