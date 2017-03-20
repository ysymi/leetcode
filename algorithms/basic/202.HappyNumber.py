class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def replace_with_sum(n):
            ret = 0
            for d in str(n):
                ret += int(d) * int(d)
            return ret

        exists_set = set([n])
        while True:
            new_n = replace_with_sum(n)
            if new_n == 1:
                return True
            if new_n in exists_set:
                return False
            exists_set.add(new_n)
            n = new_n
