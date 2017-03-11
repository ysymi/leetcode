class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def has_equal_num(s):
            s = ''.join(sorted(s)).strip('.')
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    return True
            return False

        for i in range(9):
            row = board[i]
            line = ''.join([r[i] for r in board])
            if has_equal_num(row) or has_equal_num(line):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                sq = board[j][i:i + 3] + board[j + 1][i:i + 3] + board[j + 2][i:i + 3]
                if has_equal_num(sq):
                    return False

        return True


