#! coding=utf8
# ideas:
# 
# gains:
#     def get_prime(n):
#         non_prime = set()
#         prime = []
#
#         for i in range(2, n):
#             if i not in non_prime:
#                 prime.append(i)
#
#             for p in prime:
#                 non_prime.add(i * p)
#                 if i % p == 0:
#                     break


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        is_prime = [False] * n
        prime = []

        for i in range(2, n):
            if i not in non_prime:
                prime.append(i)

            for p in prime:
                non_prime.add(i * p)
                if i % p == 0:
                    break
        print prime
        return len(prime)


print Solution().countPrimes(100000)