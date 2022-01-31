class Node:
    def __init__(self, val = None, next=None): 
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        
        if self.head:
            current = self.head
            i = 0
            while current and current.next:
                if i == index:
                    return current.val
                current = current.next
                i+=1
            if i == index:
                return current.val
        return -1       

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            current = self.head
            newNode.next = current
            current = newNode
            self.head = current
        else:
            self.head = newNode
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if self.head:
            if self.head and index > 0:
                current = self.head
                i = 0
                while current.next:
                    if i >= index - 1:
                        break
                    current = current.next
                    i+=1
                if i >= index-1 and current.next:
                    nextnode = current.next
                    current.next = newNode
                    current.next.next = nextnode
                elif i >= index-1 and not current.next:
                    current.next = newNode
            else:
                if index < 1:
                    self.addAtHead(val)
        else:
            if index < 1:
                self.head = newNode
            
    def deleteAtIndex(self, index: int) -> None:
        if self.head:
            current = self.head
            i = 0
            while current.next and current.next.next:
                if i >= index-1:
                    break
                current = current.next
                i += 1
            if i >= index-1 and current.next:
                if index <= 0:
                    self.head = current.next
                elif index >= 0:
                    current.next = current.next.next
            elif i == 0 and index == 0 and not current.next:
                self.head = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)