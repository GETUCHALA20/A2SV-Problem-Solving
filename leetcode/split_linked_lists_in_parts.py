# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        length = 0
        res = []
        while current:
            current = current.next
            length += 1
        if k >= length:
            num_of_element = 1
            reminder = 0
        else:
            num_of_element = length//k
            reminder = length%k
        
        current2 = head
        i=0
        while i < k:
            count2 =0
            dummy = ListNode(0)
            ctr = dummy
            while current2:
                num_elem = num_of_element + 1 if reminder > 0 else num_of_element
                if count2 == (num_elem):
                    break
                dummy.next = ListNode(current2.val)
                current2 = current2.next
                dummy = dummy.next
                count2 += 1
            res.append(ctr.next)
            if reminder > 0:
                reminder = reminder - 1
            i+=1
    
        return res