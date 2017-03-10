class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        x, y = 0, 0
        pos = []
        for ch in s:
            pos.append((x, y, ch))
            if x == numRows - 1:
                dx, dy = -1, 1
            if x == 0:
                dx, dy = 1, 0
            x += dx
            y += dy

        return ''.join([x[2] for x in sorted(pos)])
