# ideas:
# 不用交换，直接赋值，紧凑化非零值
#
# gains:
#


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        while i < len(nums):
            nums[i] = 0
            i += 1
