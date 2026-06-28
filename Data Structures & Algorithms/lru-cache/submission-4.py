class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mru = Node(0,0)
        self.lru = Node(0,0)
        self.mru.prev = self.lru
        self.lru.next = self.mru
    def insert(self,node):
        # to insert at the begining take mru node and its temp node
        # set the prev and next pointers to point at the new node
        mruNode,mruNode_temp = self.mru.prev,self.mru
        mruNode.next = node #mru node next is the new node making it new mru
        node.next = mruNode_temp #the end 
        node.prev = mruNode #the new prev
        mruNode_temp.prev = node #the ends prev



    def get(self, key: int) -> int:
        if key in self.cache:  
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    
    def remove(self, node):
        # removing a node requires changing the prev node to point to its  next node
        previous_node,next_node = node.prev,node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        # /if at greatere than capacitu
        if len(self.cache) >  self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]

        

