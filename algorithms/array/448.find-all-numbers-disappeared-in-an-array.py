class Solution(object):
    def findDisappearedNumbers(self, nums):
        ret = []
        for pos in xrange(len(nums)):
            i = pos
            while nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i, num in enumerate(nums):
            if i + 1 != num:
                ret.append(i + 1)
        return list(set(ret))
