# coding=utf8
# ideas:
# 所有循环的问题 double 总是会让问题简单
#
# gains:
#

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        nums = []
        for time in timePoints:
            num = int(time.replace(':', ''))
            num = num / 100 * 60 + num % 100
            nums.append(num)
        nums.sort()
        nums += [num + 24 * 60 for num in nums]
        ret = nums[1] - nums[0]
        for i in range(1, len(nums)):
            ret = min(nums[i] - nums[i - 1], ret)
        return ret
