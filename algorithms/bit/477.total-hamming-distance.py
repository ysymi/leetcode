# coding=utf8
# ideas:
# n^2的算法肯定是不行 要考虑每个数和其他数的difference
#
# gains:
#


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = [0] * 32

        for num in nums:
            d = 0
            while num != 0:
                ones[d] += num & 1
                num >>= 1
                d += 1

        tot = len(nums)
        ret = 0

        for one_num in ones:
            ret += one_num * (tot - one_num)
        return ret
