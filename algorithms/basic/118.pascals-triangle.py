#! coding=utf8
# ideas:
#
# gains:
# 需要注意 下标不是从零开始的


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(1, numRows + 1):
            if i == 1:
                row = [1]
            elif i == 2:
                row = [1, 1]
            else:
                row = [1]
                for j in range(1, i - 1):
                    row.append(ret[i - 2][j] + ret[i - 2][j - 1])
                row.append(1)

            ret.append(row)

        return ret


print Solution().generate(3)