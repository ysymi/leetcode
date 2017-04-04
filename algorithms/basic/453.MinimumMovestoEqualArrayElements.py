#! coding=utf8
# ideas:
# 其他n-1个数都加1 等于 某个数减1
#
# gains:
#

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        min_moves = 0
        for num in nums:
            min_moves += num - min_num
        return min_moves
