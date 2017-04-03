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
