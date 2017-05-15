#! coding=utf8
# ideas:
# 题目有n+1个数，数的范围恰好是1-n,  类似静态链表的实现，
# gains:
# 链表判环和寻找环入口
# 判环：
# 两个指针，一个指针每次前进一步，另一个指针每次前进两步。如果有环，两个指针先后入环，并做一个追及问题。因为2-1=1能整除所有整数，所以两者一定会相遇。
# 寻找环入口:
# 相遇后，一个指针回到起点，另一个指针位置不变。两个指针重新前进，每次均前进一步。再次相遇的地方就是环入口
# 有点神奇 详情见这里：http://blog.sina.com.cn/s/blog_6a0e04380101a9o2.html
# 其实也可以不用这种复杂的方法 因为是一个静态链表，实际上可以记录访问过的节点, 如果再次访问了，那一定就是一个重复的数字


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        next = 0
        while nums[next] != -1:
            nums[next], next = -1, nums[next]
            print nums
        return next

# class Solution(object):
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         fast = nums[nums[0]]
#         slow = nums[0]
#
#         while fast != slow:
#             fast = nums[nums[fast]]
#             slow = nums[slow]
#
#         fast = 0
#
#         while fast != slow:
#             fast = nums[fast]
#             slow = nums[slow]
#
#         return slow
#
#
#
