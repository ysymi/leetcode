#! coding=utf8
# ideas:
# 面积等于底乘高 取两个指针分别表示左和右，从两边开始逼近所有的可能，
# 因为底变短了，靠近的时候应该选择更高的，高应该是两者里边小的那个，所以移动那个矮的
# gains:
# 


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ret = 0
        while left < right:
            h = min(height[left], height[right])
            ret = max(ret, h * (right - left))
            if height[left] <= h:
                left += 1
            else:
                right -= 1
        return ret
