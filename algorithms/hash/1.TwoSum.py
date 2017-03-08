class Solution(object):
    def twoSum(self, nums, target):
     """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    pos = dict()
    for index, num in enumerate(nums):
        if num not in pos:
            pos[num] = [index]
        else:
            pos[num].append(index)

    for num in nums:
        rest = target - num
        if rest in pos:
            if rest == num:
                if len(pos[num]) == 2:
                    return pos[num]
            else:
                return sorted([pos[rest][0], pos[num][0]])


# [1,1] 2
# [2,3,4] 6
