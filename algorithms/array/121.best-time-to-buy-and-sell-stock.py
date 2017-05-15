#! coding=utf8
# ideas:
# 只交易一次，找到每天以前最低的价格，然后取最大就好
# gains:
#

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        mins = [prices[0]]
        for i in range(1, len(prices)):
            mins.append(min(prices[i], mins[i-1]))

        ret = 0
        for i in range(1, len(prices)):
            ret = max(prices[i] - mins[i], ret)
        return ret

