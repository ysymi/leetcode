# coding=utf8
# ideas:
#
# gains:
#


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {chr(v): v - 65 + 1 for v in range(65, 65 + 26)}
        ret = 0
        for ch in s:
            ret = ret * 26 + vals.get(ch)
        return ret


print Solution().titleToNumber('AAA')