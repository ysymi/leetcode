#! coding=utf8
# ideas:
# a <= b <= c <= d, d - a = (d - c) + (c - b) + (b - a)
# 现实生活中不知道未来的价格，倘若知道了就能用获取每一个价格上升的序列了，用最高的减去最低的。也就是期间每一天减去后一天的和
# gains:
#

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(1,len(prices)):
            ret += max(prices[i]-prices[i-1], 0)
        return ret
