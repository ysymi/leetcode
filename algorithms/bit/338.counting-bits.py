#! coding=utf8
# ideas:
#
#
# gains:
#


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ones = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]  # one in 0-15

        def get_ones(n):
            ret = 0
            while n:
                ret += ones[n & 15]
                n >>= 4
            return ret

        return map(get_ones, xrange(num + 1))