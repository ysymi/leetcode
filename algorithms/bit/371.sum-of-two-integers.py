#! coding=utf8
# ideas:
#
# gains:
# a + b = a ^ b + (a & b) << 1
# a' = a ^ b
# b' = (a & b) << 1
# 不断的重复这个步骤 知道b' 等于0 的时候
# oj 上的 int 都是32 位 的 所以需要纠正到32位以内


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7fffffff
        MASK = 0xffffffff

        if b == 0:
            return a if a <= MAX else ~(a ^ MASK)

        s = (a ^ b) & MASK
        c = ((a & b) << 1) & MASK

        return self.getSum(s, c)
