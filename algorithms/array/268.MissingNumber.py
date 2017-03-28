class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = sum(nums)
        sum_0_n = len(nums) * (len(nums) + 1) / 2
        return sum_0_n - sum_nums
