class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lefts = ('{', '[', '(')
        rights = ('}', ']', ')')
        stack = list(['#'])

        for ch in s:
            if ch in rights and stack[-1] == lefts[rights.index(ch)]:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 1
