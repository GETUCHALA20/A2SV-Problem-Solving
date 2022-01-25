# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = l1.val + l2.val
        
        cummulative = ListNode(val%10)
        reminder = val // 10
            
        l1 = l1.next
        l2 = l2.next
        
        cummulative_counter = cummulative
        while l1 and l2:
            val = l1.val + l2.val + reminder
            cummulative_counter.next = ListNode(val%10)
            cummulative_counter = cummulative_counter.next
            reminder = val // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = l1.val + reminder
            cummulative_counter.next = ListNode(val%10)
            cummulative_counter = cummulative_counter.next
            reminder = val // 10
            l1 = l1.next
        while l2:
            val = l2.val + reminder
            cummulative_counter.next = ListNode(val%10)
            cummulative_counter = cummulative_counter.next
            reminder = val // 10
            l2 = l2.next
        if reminder > 0:
            cummulative_counter.next = ListNode(reminder)
            cummulative_counter = cummulative_counter.next
            
        return cummulative