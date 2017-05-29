#! coding=utf8
# ideas:
# 只有一个最大值，利用2分查找，不断向中间靠拢，需要说明的是 (right + left) / 2 是中间偏左，
# gains:
#


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right ) / 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left
