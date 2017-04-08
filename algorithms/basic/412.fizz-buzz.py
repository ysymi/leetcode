#! coding=utf8
# ideas:
# 
# gains:#
# 


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(1,n+1):
            if i % 3 and i % 5:
                ret.append(str(i))
            elif i % 3 == 0 and i % 5 != 0:
                ret.append('Fizz')
            elif i % 5 == 0 and i % 3 != 0:
                ret.append('Buzz')
            else:
                ret.append('FizzBuzz')
        return ret