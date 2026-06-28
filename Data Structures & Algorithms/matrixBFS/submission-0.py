class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        Rows,Cols = len(grid),len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == Rows-1 and c == Cols -1:
                    return length
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr,dc in neighbors:
                    if (min(dr+r,dc+c) < 0 or 
                    (dr+r,dc+c) in visited or dr+r == Rows or 
                    dc+c == Cols or grid[dr+r][dc+c] == 1):
                        continue
                    queue.append((dr+r,dc+c))
                    visited.add((dr+r,dc+c))
            length+=1
        return -1
                    