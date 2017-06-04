#! coding=utf8
# ideas:
# 每一轮消除一个边界
# gains:
# 


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        left, top, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1

        d = 0
        ret = []
        while left <= right and top <= bottom:
            if d == 0:
                for i in range(left, right + 1):
                    ret.append(matrix[top][i])
                top += 1

            if d == 1:
                for i in range(top, bottom + 1):
                    ret.append(matrix[i][right])
                right -= 1
            if d == 2:
                for i in reversed(range(left, right + 1)):
                    ret.append(matrix[bottom][i])
                bottom -= 1

            if d == 3:
                for i in reversed(range(top, bottom + 1)):
                    ret.append(matrix[i][left])
                left += 1

            d = (d + 1) % 4

        return ret
