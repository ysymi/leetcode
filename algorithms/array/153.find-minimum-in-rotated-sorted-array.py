#! coding=utf8
# ideas:
#
# gains:
# 这种旋转后的数组
# [left, right] 区间有三种可能
# 1. 完全顺序，那么最小值在最左边
# 2. mid的值比两端的值都大，说明最小值在右半段
# 3. mid的值比两端的值都小，说明最小值在左半段


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
