# coding=utf8
# ideas:
# 2^10次方个数 规模不大 直接打表
#
# gains:
# 会议起一些 位运算技巧

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        from collections import defaultdict

        def get_ones(n):
            ret = 0
            while n != 0:
                ret += n & 1
                n >>= 1
            return ret

        table = defaultdict(list)
        for n in range(0, 1024):
            ones = get_ones(n)
            hours, minute = n >> 6, n & 63

            if hours < 12 and minute < 60:
                table[ones].append('%d:%02d' % (hours, minute))

        return table[num]
