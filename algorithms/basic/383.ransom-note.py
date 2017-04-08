#! coding=utf8
# ideas:
# 判断是否包含
#
# gains:
#


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = {}
        for ch in magazine:
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1

        for ch in ransomNote:
            if ch not in counter:
                return False
            if counter[ch] == 0:
                return False
            counter[ch] -= 1

        return True

