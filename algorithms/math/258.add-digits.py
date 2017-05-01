#! coding=utf8
# ideas:
# 好像是有个结论 而且是对于任意N进制都会有这个
# gains:
# 证明的核心部分在此
# an 10-base integer like 100a+10b+c, then (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        return num % 9 if num % 9 else (9 if num else 0)