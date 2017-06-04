#! coding=utf8
# ideas:
# 斐波那契数
# gains:
# 


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b

        return a
