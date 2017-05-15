#! coding=utf8
# ideas:
# 这个题目其实是在考dfs的剪枝，但是显然用python的combinations也很优雅，如果要卡时间就要自己写了
# gains:
#

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        all_comb = combinations(range(1,10), k)
        return [list(comb) for comb in all_comb if sum(comb) == n]
