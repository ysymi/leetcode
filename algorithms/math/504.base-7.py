# coding=utf8
# ideas:
# counter 简单应用 异序同构词
#
# gains:
#

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            sign = -1
            num *= -1
        else:
            sign = 1

        ret = ''
        while True:
            ret += str(num % 7)
            num /= 7
            if num == 0:
                break

        ret = ''.join(reversed(ret))
        return ret if sign == 1 else '-' + ret
