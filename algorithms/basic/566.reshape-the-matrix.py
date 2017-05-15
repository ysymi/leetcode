#! coding=utf8
# ideas:
# 
# gains:
# 


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        cr, cc = len(nums), len(nums[0])
        if cr * cc != r * c:
            return nums

        data = reduce(lambda x, y: x + y, nums)
        ret = []
        for i in range(r):
            ret.append(list(data[i * c:(i + 1) * c]))
        return ret


print Solution().matrixReshape([[1, 2], [3, 4]], r=1, c=4)
