#! coding=utf8
# ideas:
# 回溯法 就是栈式思路 进去看看再出来
# gains:
#


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import copy

        l = len(nums)
        ret = []

        def dfs(start):
            if start == l:
                ret.append(copy.deepcopy(nums))
            for i in range(start, l):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        dfs(0)
        return ret

print Solution().permute([1,2,3])