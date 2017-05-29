#! coding=utf8
# ideas:
# 最简单的办法就是 全部翻转然后 分成两部分分别翻转
# gains:
#


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(nums):
            n = len(nums)
            for i in range(n / 2):
                nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
            return nums

        n = len(nums)
        k %= n

        if k != 0:
            nums = reverse(nums)
            nums[:k] = reverse(nums[:k])
            nums[k:] = reverse(nums[k:])
