#! coding=utf8
# ideas:
# 1. 用对数判断
# 2. 用一个很大的3的幂去整除 能整除说明这个数是由3构成的（考虑质数分解）
# gains:
# 


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0:
            return False

        i = math.log(n, 3)
        return abs(i - int(i + 0.5)) < 1e-10  # 判断是不是整数
