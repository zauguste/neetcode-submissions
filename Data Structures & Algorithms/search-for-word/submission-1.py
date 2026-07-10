class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,col,char):
            # reach the end of word
            if char == len(word):
                return True
            # out of bounds and reached a character not in word
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[char]:
                return False
            # temperary hold board and mark visited
            temp, board[row][col] = board[row][col], '/'
            res = dfs(row + 1, col, char + 1) or dfs(row - 1, col, char + 1) or dfs(row, col + 1, char + 1) or dfs(row, col - 1, char + 1)
            board[row][col] = temp

            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row,col,0):
                        return True
        return False
        



