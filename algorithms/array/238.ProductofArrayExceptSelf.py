class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = [1] + nums + [1]
        left, right = [1] * (n + 2), [1] * (n + 2)

        for i in xrange(1, n + 1):
            left[i] = left[i - 1] * nums[i]

        for i in xrange(n, 0, -1):
            right[i] = right[i + 1] * nums[i]

        ret = []
        for i in xrange(1, n + 1):
            ret.append(left[i - 1] * right[i + 1])
        return ret
