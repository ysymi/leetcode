#! coding=utf8
# ideas:
# 
# gains:#
# 


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.lower() == word or word.upper() == word:
            return True
        if word[0] >= 'A' and word[1:] == word[1:].lower():
            return True
        return False