#! coding=utf8
# ideas:
# 打表 预处理出4位数字的所有情况 然后每次取4位判断
# gains:
# 


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111
        table = [
            0, 1, 1, 2,
            1, 2, 2, 3,
            1, 2, 2, 3,
            2, 3, 3, 4
        ]

        ret = 0
        for shift in range(0, 32, 4):
            ret += table[(n >> shift) & 15]
        return ret
