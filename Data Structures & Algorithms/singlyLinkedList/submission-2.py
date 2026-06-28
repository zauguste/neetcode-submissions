class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    #                     i=0 index = 0
    # # s.h->[-1|.next]->[n1|.next]-> None
    #                     #s.t
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
                    # /-----------------\
    # # s.h->[-1|.next]->   |newNode|.next -> [n1|.next]-> None
    #                     #s.t
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)   
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i<index and curr:
            i+=1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
