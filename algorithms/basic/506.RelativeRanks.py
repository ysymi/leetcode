class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        for idx, num in enumerate(nums):
            nums[idx] = (num, idx)

        nums.sort(reverse=True)

        top_three = ['Gold Medal', "Silver Medal", "Bronze Medal"]
        for idx, num in enumerate(nums):
            if idx < 3:
                rank = top_three[idx]
            else:
                rank = str(idx + 1)
            nums[idx] = (num[1], rank)  # original position and rank

        nums.sort()

        return [x[1] for x in nums]
