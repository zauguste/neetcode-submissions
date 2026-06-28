class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru,self.mru = Node(0,0),Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru
    # remove
    # take the previous_node and the next_node
    # make the previous next = the removing_nodes next
    # make the removing node's  next node the previous node
    def remove(self,node):
        previous_node,next_node = node.prev,node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        # [0,0]-> [0,0] -> <-[0,0]mru_temp
    # insert
    # take the mru and the mru temp, we want to put the new node between them
    # make the mru.next = newnode
    # make the new node next = mru temp to indicate we're at the end
    # make the mru_temp previous = newnode
    # make the new_node previous the mru node

    def insert(self,node):
        mru, mru_temp = self.mru.prev, self.mru
        mru.next = node
        node.prev = mru
        node.next = mru_temp
        mru_temp.prev = node

        


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]

            
        
