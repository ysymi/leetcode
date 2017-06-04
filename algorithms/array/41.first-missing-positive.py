#! coding=utf8
# ideas:
# 给n个数 找出其中没出现的最小正整数
# 1. 这n个数 是1-n 占完了最小的n个正整数 那最小未出现的正整数就是n+1
# 2. 只要有一个数不是1-n中的一个数，那这个数就是没出现的最小正整数
# 综上 只要把数组中每一个数放到他对应顺序的位置上，比如说2就放到下标为2 的位置上，5就放到下标为5的位置上，
# 最后第一个没有出现在应该出现位置上的人，就是最小未出现的数
#
# gains:
# 冷静分析的典型案例
# 还有一个 O(n) 空间复杂度的算法
# 可以统计 1-n 出现次数，也很好理解
#

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        for i in range(l):
            # nums[i]-1 应该在的位置
            # 不断将nums[i] 这个数 放在 nums[i] - 1 这个位置上
            while 0 < nums[i] < l and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(l):
            if nums[i] != i + 1:
                return i + 1

        return l + 1
