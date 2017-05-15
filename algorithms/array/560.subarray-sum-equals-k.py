#! coding=utf8
# ideas:
# 区间和问题可以用前缀和的差来计算得到，这个题恰好是这种场景。counter记录了在某个位置以前的前缀和有多少种不同的构造方式。以此来获取以这个位置为结尾的，和为k的子数组的个数
# gains:
#

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        counter = Counter([0])
        prefix_sum = 0
        ret = 0

        for num in nums:
            prefix_sum += num
            ret += counter[prefix_sum - k]
            counter[prefix_sum] += 1

        return ret
