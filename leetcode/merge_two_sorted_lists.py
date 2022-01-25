# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        marker1 = list1
        marker2 = list2
        
        if marker1 is None:
            return marker2
        if marker2 is None:
            return marker1

        if marker1.val < marker2.val:
            res = ListNode(marker1.val)
            marker1 = marker1.next
        else:
            res = ListNode(marker2.val)
            marker2 = marker2.next

        ptr = res
        
        while marker1 and marker2:
            if marker1.val <= marker2.val:
                temp = ListNode(marker1.val)
                ptr.next = temp
                marker1 = marker1.next
                ptr = ptr.next
            else:
                temp = ListNode(marker2.val)
                ptr.next = temp
                marker2 = marker2.next
                ptr = ptr.next
        
        if marker1:
            ptr.next = marker1
            
        if marker2:
            ptr.next = marker2
        return res