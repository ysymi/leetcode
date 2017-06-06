#! coding=utf8
# ideas:
# 1. 用对数判断
# 2. 用一个很大的3的幂去整除 能整除说明这个数是由3构成的（考虑质数分解）
# gains:
# 判断 是不是2的整数幂 n&(n-1) == 0
# n&(n-1) 表示x最低位1变成0 后的数字
# n = n&(n-1) 就会让n 最低位1变成0


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
