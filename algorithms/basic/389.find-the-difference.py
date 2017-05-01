#! coding=utf8
# ideas:
# 应该用少的一个去比较
# gains:
# 


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = sorted(s), sorted(t)
        for idx, ch in enumerate(s):
            if ch != t[idx]:
                return t[idx]
        return t[-1]