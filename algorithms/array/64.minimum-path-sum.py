#! coding=utf8
# ideas:
# 简单DP
# gains:
#


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        dp = [[ 0 for j in range(c)] for i in range(r)]

        for i in range(r):
            for j in range(c):
                if j == 0 and i == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

        return dp[r-1][c-1]
