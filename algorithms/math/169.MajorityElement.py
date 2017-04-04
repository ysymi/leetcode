# coding=utf8
# ideas:
# 说的比较绕 出现次数大于一半 中位数满足这个要求
#
# gains:
#

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) / 2]