#! coding=utf8
# ideas:
# 很有规律的遍历，坐标之和依次加一，变化方向依次取反，或者是变化方向有奇偶性
#
# gains:
# 不需要的计算 尽量避免 尽量只做有效的计算


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m, n = len(matrix), len(matrix and matrix[0] or [])
        for s in range(m + n + 1):
            if s & 1 == 0:
                dx, dy = 1, -1
                y = min(s, m - 1)
                x = s - y
            else:
                dx, dy = -1, 1
                x = min(s, n - 1)
                y = s - x

            while 0 <= x < n and 0 <= y < m:
                ret.append(matrix[y][x])
                x += dx
                y += dy

        return ret

