#! coding=utf8
# ideas:
#
# gains:
# 原地随机乱序算法
# 生成随机数范围从[0,n]一直到[0,1] 把每一轮中随机出的位置与第i个位置的数字进行交换，交换后就不在变动位置i了


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.data = nums
        self.size = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random

        for i in reversed(range(1, self.size)):
            j = random.randint(0, i)
            self.data[i], self.data[j] = self.data[j], self.data[i]

        return self.data
