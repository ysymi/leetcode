#! coding=utf8
# ideas:
# 刚好可以用compress来做 不过可以知道效率不高
# gains:
# 


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import compress

        ret = []
        n = 1 << len(nums)
        for i in range(n):
            selector = [(i >> d) & 1 for d in range(len(nums))]
            ret.append(list(compress(nums, selector)))

        return ret

print Solution().subsets([1,2,3])
