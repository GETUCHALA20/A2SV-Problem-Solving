# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        first = head
        second = prev
        while second.next:
            nextnode = first.next
            first.next = second
            first = nextnode

            nextnode = second.next
            second.next = first
            second = nextnode
        