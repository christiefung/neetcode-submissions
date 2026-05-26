class Node():
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        current = self.dummy_head.next
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        prev_first = self.dummy_head.next
        new_node.prev = self.dummy_head
        new_node.next = prev_first
        self.dummy_head.next = new_node
        prev_first.prev = new_node
        self.length +=1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        prev_first = self.dummy_tail.prev
        new_node.prev = prev_first
        new_node.next = self.dummy_tail
        self.dummy_tail.prev = new_node
        prev_first.next = new_node
        self.length += 1
        


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        current = self.dummy_head.next
        for i in range(index):
            current = current.next

        new_node = Node(val)
        old_prev = current.prev
        current.prev = new_node
        new_node.prev = old_prev
        old_prev.next = new_node
        new_node.next = current

        self.length +=1


        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
            
        current.prev.next = current.next
        current.next.prev = current.prev   

        #prev_node = current.prev
        #next_node = current.next
        #prev_node.next = next_node
        #next_node.prev = prev_node

        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)