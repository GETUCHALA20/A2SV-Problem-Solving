# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        current2  = head
        n = 0
        while current:
            current = current.next
            n+=1
        
        half = n//2 
        
        while half > 0:
            current2 = current2.next
            half -= 1
        return current2
        