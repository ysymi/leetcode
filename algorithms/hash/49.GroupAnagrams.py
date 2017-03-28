class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        ret = {}
        for s in strs:
            leader = ''.join(sorted(s))
            if leader not in ret:
                ret[leader] = []
            ret[leader].append(s)

        return [v for k, v in ret.items()]
