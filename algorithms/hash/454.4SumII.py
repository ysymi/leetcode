# coding=utf8
# ideas:
# 利用hash存储一半的运算结果 空间换时间
#
# gains:
#

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter

        AB = Counter([a + b for a in A for b in B])
        CD = Counter([c + d for c in C for d in D])

        ret = 0
        for ab in AB:
            if -ab in CD:
                ret += AB[ab] * CD[-ab]
        return ret
