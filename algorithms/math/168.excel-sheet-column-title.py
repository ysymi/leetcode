# coding=utf8
# ideas:
# 微软的这个规则实在是乍一看很友好，实际上很奇怪的一个设计，
#
# gains:
#


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ''
        AtoZ = [chr(v + ord('A')) for v in range(26)]
        while n > 0:
            n -= 1
            ret += AtoZ[n % 26]
            n /= 26
        return ''.join(reversed(ret))
