#! coding=utf8
# ideas:
#
# gains:
# 最大连续子和 每个数字两种选择，要么加入到前一个数组里构成更大的数组，要么自己是最大的数组的第一个元素。
# 如果已有的数组已经是负的 那么加入到前一个数组已经不可能构造成更大的数组了



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum = num if cur_sum < 0 else cur_sum + num
            max_sum = max(max_sum, cur_sum)

        return max_sum

