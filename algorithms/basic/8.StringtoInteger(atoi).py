class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        val = 0
        sign = 1
        str = str.strip()

        if len(str) <= 0:
            return 0

        if str[0] == '-':
            sign = -1
        if str[0] in '-+':
            str = str[1:]

        for i in str:
            if i in '0123456789':
                val = int(i) + val * 10
            else:
                break

        ret = val * sign
        if ret > (1 << 31) - 1:
            ret = (1 << 31) - 1
        elif ret < -(1 << 31):
            ret = -(1 << 31)

        return ret
