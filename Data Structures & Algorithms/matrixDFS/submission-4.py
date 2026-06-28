class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        #get dim
        Rows,Cols = len(grid), len(grid[0])
        visited = set()
        def dfs(grid,r,c,visited):
            if (min(r,c) < 0 or r == Rows or c == Cols or grid[r][c] == 1 or (r,c) in visited):
                return 0
            if r == Rows-1 and c == Cols-1:
                return 1
            count = 0
            visited.add((r,c))
            count += dfs(grid,r+1,c,visited)
            count += dfs(grid,r-1,c,visited)
            count += dfs(grid,r,c+1,visited)
            count += dfs(grid,r,c-1,visited)
            visited.remove((r,c))
            return count
        return dfs(grid,0,0,visited)
            