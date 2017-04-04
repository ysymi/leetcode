# coding=utf8
# ideas:
# counter简单用法
#
# gains:
# 以后不手写counter了


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        counter = Counter(s)
        for i, ch in enumerate(s):
            if counter.get(ch, 0) == 1:
                return i
        return -1
