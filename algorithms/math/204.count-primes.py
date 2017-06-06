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

        deleted = [False] * n
        prime = []

        for i in range(2, n):
            if not deleted[i]:
                prime.append(i)

            for p in prime:
                if i * p < n:
                    deleted[i * p] = True
                    if i % p == 0:
                        break

        return len(prime)


print Solution().countPrimes(10000)