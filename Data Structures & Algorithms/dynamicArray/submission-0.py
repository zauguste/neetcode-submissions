class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # 1. check if we are at capacity if so resize
        # 2. insert into the end 
        # 3. increase the size
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size+=1

    def popback(self) -> int:
        #1. decrement the size
        #2. return that end
        if self.size >0:
            self.size -=1
        return self.arr[self.size]

    def resize(self) -> None:
        # 1. double cap
        # 2. create new space 
        # 3. insert into new space
        # 4. point to the new space
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity