# ideas:
# 均值定理？尽可能让两个数相等
#
# gains:
# 尽快返回


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        for d in xrange(int(math.sqrt(area)), 0, -1):
            if area % d == 0:
                return [area/d, d]
