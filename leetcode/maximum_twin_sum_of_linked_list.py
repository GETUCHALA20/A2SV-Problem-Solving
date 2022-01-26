# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list1 = []
        current = head
        while current:
            list1.append(current.val)
            current = current.next
        maximum = 0
        length = len(list1)
        for i in range(length//2):
            val = list1[i]+list1[length-1-i]
            if val > maximum:
                maximum = val
        return maximum