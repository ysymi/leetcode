#! coding=utf8
# ideas:
# floodfill 走一遍
# gains:
# 


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        r, c = len(grid), len(grid[0])
        visit = [[False for _ in range(c)] for _ in range(r)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def dfs(x, y):
            visit[x][y] = 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '1' and not visit[nx][ny]:
                    dfs(nx, ny)

        ret = 0
        for i in range(r):
            for j in range(c):
                if not visit[i][j] and grid[i][j] == '1':
                    ret += 1
                    dfs(i, j)

        return ret