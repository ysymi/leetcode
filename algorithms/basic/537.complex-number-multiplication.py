# coding=utf8
# ideas:
#
#
# gains:
#


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import re
        pattern = re.compile(r'([+-]?\d+)\+([+-]?\d+)i')
        a1, a2 = map(int, pattern.search(a).groups())
        b1, b2 = map(int, pattern.search(b).groups())

        a = a1 * b1 - a2 * b2
        b = a2 * b1 + a1 * b2
        return '%d+%di' % (a, b)
