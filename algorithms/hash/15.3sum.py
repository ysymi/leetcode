#! coding=utf8
# ideas:
# 降到n^2 注意去重问题
# gains:
# 


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        pos = {}
        for i, num in enumerate(nums):
            pos[num] = i

        ret = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                num = - (nums[i] + nums[j])
                if num in pos and pos[num] > j:
                    k = pos[num]
                    ret.append([nums[i], nums[j], nums[k]])
        return ret