#! coding=utf8
# ideas:
#
#
# gains:
# any 和 all 是对元素 为真的判断


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        return any(map(lambda x: x > 1, Counter(nums).values()))
