# coding=utf8
# ideas:
# counter 简单应用 异序同构词
#
# gains:
#


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter

        return Counter(s) == Counter(t)

int