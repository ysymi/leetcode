#! coding=utf8
# ideas:
# 
# gains:#
# 


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxy = len(grid)
        maxx = len(grid[0]) if maxy > 0 else 0

        def get_board(x, y):
            ret = 0
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < maxx and 0 <= ny < maxy:
                    if grid[ny][nx] == 0:
                        ret += 1
                else:
                    ret += 1
            return ret

        ret = sum(get_board(x, y) for x in range(maxx) for y in range(maxy) if grid[y][x] == 1)
        return ret