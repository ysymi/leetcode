class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for pos in xrange(len(nums)):
            i = pos
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
            if i != nums[i] - 1:
                ret.append(nums[i])
        return list(set(ret))
