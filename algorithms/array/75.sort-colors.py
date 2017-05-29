#! coding=utf8
# ideas:
# p1是1开始的地方, p2是2开始的地方, 只需要把0往前调，把2往后调
# gains:
#


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1, p2, i = 0, len(nums) - 1, 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                i -= 1
            i += 1

