# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        marker = head
        while marker and marker.next:
            nextnode = marker.next
            if marker.val == nextnode.val:
                marker.next = nextnode.next
            else:
                marker = marker.next
                
        return head