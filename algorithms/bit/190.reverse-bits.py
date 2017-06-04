#! coding=utf8
# ideas:
# 手动交换对称位
# gains:
# set      num |= (1<<bit)
# clear    num &= ~(1<<bit)


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        for i in range(16):
            hbit = (n >> (31 - i)) & 1
            lbit = (n >> i) & 1
            if hbit != lbit:
                if hbit == 1:
                    n &= ~(1 << (31 - i))
                    n |= (1 << i)
                else:
                    n |= 1 << (31 - i)
                    n &= ~(1 << i)
        return n
