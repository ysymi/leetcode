#! coding=utf8
# ideas:
# 只是判断有没有 并不需要找出来所有的 三元组
# 如果有的话 一定是 存在一个数 它左边有一个比他小的 右边有一个比他大的
# 那我们取极端，用[左边最小值, 它自己，右边最大值]判断，如果存在，那么一定存在这样的三元组
# gains:
# 


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l < 3:
            return False
        lmin = [nums[0]] * l
        rmax = [nums[l - 1]] * l

        for i in range(1, l):
            lmin[i] = min(lmin[i - 1], nums[i])
        for i in range(l - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], nums[i])

        for i in range(1, l - 1):
            if lmin[i - 1] < nums[i] < rmax[i + 1]:
                return True
        return False