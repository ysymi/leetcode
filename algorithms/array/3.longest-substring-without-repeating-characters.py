class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end, length = 0, 0, len(s)
        counter = set()
        ret = 0

        while start < length:

            while end < length:
                if s[end] in counter:
                    break
                counter.add(s[end])
                ret = max(ret, end - start + 1)
                end += 1

            counter.remove(s[start])
            start += 1

        return ret
