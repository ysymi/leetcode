#! coding=utf8
# ideas:
# 题意：每一对的最小值的和尽可能大。贪心，尽可能两个数的差距尽量小。
# gains:#
# 


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(num for idx, num in enumerate(sorted(nums)) if idx & 1 == 0)
