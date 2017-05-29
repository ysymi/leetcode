#! coding=utf8
# ideas:
#
# gains:
# 据说是可以先沿着左下-右上的对角线进行翻转，再上下进行翻转就可以了
# 据说是平面旋转的折叠定理

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        if n > 1:

            for i in range(n):
                for j in range(n - i):
                    matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i],  matrix[i][j]

            m = n / 2
            for i in range(m):
                matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
