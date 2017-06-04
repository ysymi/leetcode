#! coding=utf8
# ideas:
# 每一列的水量可以是 两边最高的柱子中矮的一个和自己这一列的柱子的插来决定
# gains:
# 


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        lh, rh = [-1] * l, [-1] * l

        for i in range(1, l - 1):
            lh[i] = max(lh[i - 1], height[i - 1])

        for i in range(l - 2, 0, -1):
            rh[i] = max(rh[i + 1], height[i + 1])

        ret = 0
        for i in range(l):
            h = min(lh[i], rh[i])
            if height[i] < h:
                ret += h - height[i]

        return ret
