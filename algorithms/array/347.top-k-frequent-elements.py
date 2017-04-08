# ideas:
# 对出现次数进行排序
#
# gains:
# items是一个方法而不是属性，需要调用才返回list，
# reverse和key可能不需要同时出现，因为有些时候，key可以包括reverse的功能


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
