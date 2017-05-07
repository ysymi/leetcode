#! coding=utf8
# ideas:
# 利用并查集解决 需要注意的是 这回需要统计树个数 如果想要同father值判断，需要将
# gains:
#


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        n = len(M[0])
        fa = list(range(n))

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            fx = find(x)
            fy = find(y)
            if fx != fy:
                fa[fy] = fx

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    union(i, j)

        map(find, range(n))  # important

        return len(set(fa))
