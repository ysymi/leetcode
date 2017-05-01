#! coding=utf8
# ideas:
# 字典基于key排序的简单应用
# gains:
# 


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counter = [(v,k) for k,v in Counter(s).items()]
        return ''.join([k*v for v,k in sorted(counter, reverse=True)])