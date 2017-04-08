# coding=utf8
# ideas:
#
#
# gains:
#


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        import math
        if num == 0:
            n = 1
        else:
            n = int(math.ceil(math.log(num, 2)))
        return ~num & ((1 << n) - 1)


print Solution().findComplement(10)
