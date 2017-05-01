#! coding=utf8
# ideas:
# 每回都计算这次攻击效果。如果将多个线段合并计算，有可能最后一次会漏掉，需要特判，不优雅
# gains:
# 


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        ret = 0
        last_st, last_ed = 1, 1
        for this_st in timeSeries:
            this_ed = this_st + duration
            if last_st <= this_st < last_ed:
                ret += this_ed - last_ed
            else:
                ret += this_ed - this_st
            last_st, last_ed = this_st, this_ed
        return ret
