class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def read_off(s):
            s += '#'
            ret = ''
            cur_ch = s[0]
            cur_count = 0

            for ch in s:
                if ch == cur_ch:
                    cur_count += 1
                else:
                    ret += str(cur_count) + str(cur_ch)
                    cur_count = 1
                    cur_ch = ch
            return ret

        last = '1'
        for i in xrange(n - 1):
            last = read_off(last)
        return last

