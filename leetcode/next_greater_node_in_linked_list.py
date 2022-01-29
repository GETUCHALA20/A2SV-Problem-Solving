# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        current = head
        stack = []
        i = 0
        while current:
            if len(stack) == 0:
                stack.append((current.val,i))
                res.append(0)
            else:
                while len(stack) > 0 and stack[-1][0] < current.val:
                    val = stack.pop()
                    res[val[-1]] = current.val
                res.append(0)
                stack.append((current.val,i))
            i+=1
            current = current.next
        return res
                