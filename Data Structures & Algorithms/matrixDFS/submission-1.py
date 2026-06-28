class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        Rows,Cols = len(grid),len(grid[0])
    
        def dfs(visited,grid,r,c):
            if (min(r,c) < 0 or r == Rows or c == Cols or (r,c) in visited or grid[r][c] == 1):
                return 0
            if r == Rows - 1 and c == Cols - 1: #grie[r][c] == 0: it was supposed to be ( and ) grie[r][c] == 0 has nothing to do with this
                return 1
            visited.add((r,c))
            # count might have to go here too
            # count needs to equal 0
            count = 0 
            count += dfs(visited,grid,r+1,c)
            count += dfs(visited,grid,r-1,c)
            count += dfs(visited,grid,r,c+1)
            count += dfs(visited,grid,r,c-1)
            visited.remove((r,c))
            return count

        return dfs(set(),grid,0,0)