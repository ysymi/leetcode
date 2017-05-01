#! coding=utf8
# ideas:
# 每一个单词反序就好
# gains:#
#

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        for word in s.split():
            ret.append(word[::-1])
        return ' '.join(ret)

