class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 32bit: 0-2^31-1, -1~-2^31

        value = abs(x)
        sign = x >= 0 or -1
        reverse_value = int(str(value)[::-1])
        reverse_x = reverse_value * sign
        if -1 * 1 << 31 <= reverse_x < 1 << 31:
            return reverse_x
        else:
            return 0
