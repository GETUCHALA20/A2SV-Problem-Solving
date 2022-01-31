# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randrange
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        current = self.head
        random = self.head
        i = 0
        while current:
            current = current.next
            i+=1
            
        z = randrange(0,i)
        
        for _ in range(z):
            random = random.next
        return random.val
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()