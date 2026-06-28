class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru,self.mru = Node(0,0), Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

# insert most recenlty used to the right: 
# take right temp and right temp prev
# right temp prev.next = nmr.next = right_temp
# nmr.prev,right_temp_prev.next = right_temp_prev,nmr
#             mru                     mru_temp
# Node(0,0), <-node-> <- newnode-> <-Node(0,0)
    def insert(self,node):
        mru, mru_temp = self.mru.prev, self.mru
        mru_temp.prev = node 
        node.next = mru_temp
        node.prev = mru
        mru.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
# previous_node and removing_node_next =
# previous_node.next = removing_node_next
# removing_node_next.prev = previous_node
    def remove(self, node):
        previous_node, removing_node_next = node.prev, node.next
        previous_node.next = removing_node_next
        removing_node_next.prev = previous_node


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
            # take least recently used
            # remove it from the node list
            # delete it from the cache
#  left temp   right_temp_prev                     right_temp
# <-[0,0]->... <-[1,1]->  <-[new most recent] ->   <-[0,0]->

# insert most recenlty used to the right: 
# take right temp and right temp prev
# right temp prev.next = nmr.next = right_temp
# nmr.prev,right_temp_prev.next = right_temp_prev,nmr


# previous_node                 removing_node_next
# <-[0,0]->  <-[node_removing]->       <-[0,0]->
# remove
# previous_node and removing_node_next =
# previous_node.next = removing_node_next
# removing_node_next.prev = previous_node