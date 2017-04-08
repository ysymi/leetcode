class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        last, cur = 0, 0
        for i in nums:
            cur += i
            if cur > last:
                ret = max(cur, ret)
                last = cur
            else:
                last = cur = 0

        return ret
