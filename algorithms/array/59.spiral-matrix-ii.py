#! coding=utf8
# ideas:
# 
# gains:
# 


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [list(range(1, n + 1)) for _ in range(n)]

        num = 1
        depth = 0
        dx = [0, 1, 0, -1]  # row
        dy = [1, 0, -1, 0]  # column

        for length in range(n - 1, -1, -2):
            x, y = depth, depth
            depth += 1
            if length == 0:
                matrix[x][y] = num

            for i in range(4):
                for _ in range(length):
                    matrix[x][y] = num
                    x += dx[i]
                    y += dy[i]
                    num += 1
        return matrix


print Solution().generateMatrix(5)
