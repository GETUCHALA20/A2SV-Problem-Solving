# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head
        prev = None
        if not head or head.next == None:
            return None
        
        for i in range(n-1):
            right = right.next
        
        while right.next:
            prev = left
            left = left.next
            right = right.next
        if prev:
            prev.next = left.next
        else:
            left = left.next
            return left
        
        return head