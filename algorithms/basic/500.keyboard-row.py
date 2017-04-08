#! coding=utf8
# ideas:
# 
# gains:#
# 


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = dict()
        row.update(dict.fromkeys('qwertyuiop', 1))
        row.update(dict.fromkeys('asdfghjkl', 2))
        row.update(dict.fromkeys('zxcvbnm', 3))

        ret = []
        for word in words:
            word_ori = word
            word = word.lower()

            for i in range(len(word)-1):
                if row[word[i]] != row[word[i+1]]:
                    break
            else:
                ret.append(word_ori)
        return ret