#! coding=utf8
# ideas:
# 取两个指针不断往后移 确定的区间小时 后一个值往后移 大时 前一个指往后移
# gains:
# 


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        ret = len(nums) + 1
        sum = 0
        left, right = 0, 0
        n = len(nums)
        while left < n:
            if sum < s:
                if right < n:
                    sum += nums[right]
                    right += 1
            else:
                ret = min(ret, right - left)
                print right, left, sum
                sum -= nums[left]
                left += 1

            print left, right

        return ret


print Solution().minSubArrayLen(7, [2,3,1,2,4,3])