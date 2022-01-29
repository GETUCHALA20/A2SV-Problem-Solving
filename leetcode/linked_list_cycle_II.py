# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        marker1 = head
        marker2 = head
        while marker2 and marker2.next:
            marker1 = marker1.next
            marker2 = marker2.next.next

            if marker1 == marker2:
                break
        else:
            return None

        marker1 = head
        while marker1 != marker2:
            marker1 = marker1.next
            marker2 = marker2.next
        return marker1