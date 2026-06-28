class Graph:
    
    def __init__(self):
        # create adjacecy list
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        # check if there is a src in our adj_list
            # src -> set()
        # check if there is a dst in our adj_list
            # dst -> set()
        # src -> dst
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        # if src or dst not in adj_list return false
        # else remove and return true
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True
        # correct
    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self.d(src,dst,visited)
    def d(self,src,dst,visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adj_list.get(src,set()):
            if neighbor not in visited:
                if self.d(neighbor,dst,visited):
                    return True
        return False
