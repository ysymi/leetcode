#! coding=utf8
# ideas:
# 折半后将时间复杂度 降到n^2 发现手动判断去重和插入set的时间几乎一样
# gains:
# 


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum2 = {}
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num = nums[i] + nums[j]
                if num not in sum2:
                    sum2[num] = []
                sum2[num].append([i, j])

        ret = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num = target - (nums[i] + nums[j])
                if num not in sum2:
                    continue
                for k, l in sum2[num]:
                    if k > j:
                        ret.add((nums[i], nums[j], nums[k], nums[l]))

        return [list(qt) for qt in ret]

