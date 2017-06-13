#! coding=utf8
# ideas:
# 牛顿迭代或者2分 牛顿迭代更快一些
# gains:
# 这里和泰勒公式有点点联系
# 泰勒公式将任意函数在某个点近似表示为一个多项式
# n阶的泰勒公式在某个点近似的结果 与 原表达式的n阶导是一样的，而一阶泰勒展开就是某点的切线
# 牛顿迭代就是不断的用某点的切线与x轴交点，来代替某点，直到收敛到某一范围内，就可以认为是找到了原方程的解


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return x

        eps = 1e-6
        x0, x1 = 0.0, float(x)

        while abs(x0 - x1) > eps:
            x0 = x1
            x1 = 0.5 * (x0 + x / x0)

        return int(x0)
