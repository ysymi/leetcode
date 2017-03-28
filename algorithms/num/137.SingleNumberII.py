class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for num in nums:

            if num >= 0:
                s = [int(ch) for ch in str(num)]
            else:
                s = [int('-' + ch) for ch in str(abs(num))]

            for pos, n in enumerate(s):
                if pos not in counter:
                    counter[pos] = dict.fromkeys(list(range(-9, 10)))
                if not counter[pos][n]:
                    counter[pos][n] = 0
                counter[pos][n] += 1

        ret = 0
        for pos in sorted(counter.keys()):
            num = [k for k, v in counter[pos].items() if v and v % 3 != 0]
            if len(num):
                ret = ret * 10 + num[0]

        return ret
