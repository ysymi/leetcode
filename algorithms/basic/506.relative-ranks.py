# ideas:
# 记录下标
#
# gains:
# sort是一个iterable的原地排序，return None
# sorted是排序一个iterable的拷贝，return 排序结果 （字面意思）

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
