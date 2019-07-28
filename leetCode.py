# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        headNode = ListNode(0)
        tailNode = headNode
        remainNode = None

        carryDigit = 0
        while l1 is not None and l2 is not None:
            currentDigit = 0
            currentSum = l1.val + l2.val + carryDigit
            if currentSum >= 10:
                carryDigit = 1
                currentDigit = currentSum - 10
            else:
                currentDigit = currentSum
                carryDigit = 0
            tailNode.next = ListNode(currentDigit)
            tailNode = tailNode.next
            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            remainNode = l1
        elif l2 is not None:
            remainNode = l2

        while remainNode is not None:
            currentDigit = 0
            currentSum = remainNode.val + carryDigit
            if currentSum >= 10:
                carryDigit = 1
                currentDigit = currentSum - 10
            else:
                currentDigit = currentSum
                carryDigit = 0
            tailNode.next = ListNode(currentDigit)
            tailNode = tailNode.next
            remainNode = remainNode.next
        if carryDigit > 0:
            tailNode.next = ListNode(carryDigit)
            tailNode = tailNode.next
        return headNode.next

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        activeDict = {}
        maxLen = 0
        for i in range(len(s)):
            if s[i] in activeDict:
                curDictSize = len(activeDict)
                biggestIndexInActiveDict = i - 1
                startIndexInActiveDict = biggestIndexInActiveDict - curDictSize + 1
                for j in range(startIndexInActiveDict, activeDict[s[i]]):
                    activeDict.pop(s[j])
                activeDict[s[i]] = i
            else:
                activeDict[s[i]] = i
                if len(activeDict) > maxLen:
                    maxLen = len(activeDict)
        return maxLen

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        iMin, iMax = 0, m
        while iMin <= iMax:
            i = (iMin + iMax) / 2
            j = (m + n + 1) / 2 - i
            if i < m and nums2[j - 1] > nums1[i]:
                # i is too small, increase it
                iMin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                # i is too big, decrease it
                iMax = i - 1
            else:
                # i is perfect
                if i == 0:
                    maxOfLeft = nums2[j - 1]
                elif j == 0:
                    maxOfLeft = nums1[i - 1]
                else:
                    maxOfLeft = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return maxOfLeft
                if i == m:
                    minOfRight = nums2[j]
                elif j == n:
                    minOfRight = nums1[i]
                else:
                    minOfRight = min(nums1[i], nums2[j])
                return (maxOfLeft + minOfRight) / 2.0










def createListNodeList(nums):
    headNode = ListNode(0)
    tailNode = headNode
    for i in range(len(nums)):
        tailNode.next = ListNode(nums[i])
        tailNode = tailNode.next
    return headNode.next

solution = Solution()
answer = solution.lengthOfLongestSubstring("abcdefgabcbb")
print(answer)
