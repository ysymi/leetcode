#! coding=utf8
# ideas:
# 去除连续相似的，貌似前n个数是剩下的就行了
# gains:
# 


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        l = 0
        for i in range(len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] = nums[i]
        return l + 1