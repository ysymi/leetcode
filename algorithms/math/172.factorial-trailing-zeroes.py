#! coding=utf8
# ideas:
# 
# gains:
# 主要是5的个数决定0的数量
# 正常是 从1 到 n 检查每个数能提供多少个 5 其实这个优化为什么会变成这样 我不是很清楚。。。


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n > 0:
            ret += n / 5
            n /= 5
        return ret
