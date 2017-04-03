class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in counter[:k]]
