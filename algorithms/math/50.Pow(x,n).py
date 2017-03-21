class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 2^6 = 2^(2+4) = 2^2 * 2^4
        # 2^-6 = 1 / 2^6
        inverse = False
        if x == 0.0:
            return 0.0
        if n == 1.0:
            return x
        if n < 0:
            n = -n
            inverse = True

        ret = 1.0
        p = x
        while n != 0:
            if n & 1:
                ret *= p
            p *= p
            n /= 2

        if inverse:
            ret = 1.0 / ret
        return ret



