class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        rows, cols = len(board), len(board[0])

        path = set()

        def dfs(r, c, char_idx):
            if char_idx == len(word): # if we found the word already
                return True
            
            '''
            Cases to return False to
            1. If r and c are out of bounds at 0
            2. If r and c are out of bounds at rows and cols
            3. If that specific letter in the word is not equal to 
               the current position in board
            4. If the current possition we're at is at the path set.
               This means we went through this already and that can't happen
            '''
            if r < 0 or c < 0 or \
               r >= rows or c >= cols or \
               word[char_idx] != board[r][c] or \
               (r, c) in path:
                return False
            
            # If none of those cases were satisfied, 
            # Depth First Search will
            # continue.
            
            path.add((r, c))
            res = dfs(r + 1, c, char_idx + 1) or \
                  dfs(r - 1, c, char_idx + 1) or \
                  dfs(r, c + 1, char_idx + 1) or \
                  dfs(r, c - 1, char_idx + 1) 
            
            path.remove((r, c)) # Because we no longer need that specific postion after calling it in the DFS function

            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): # 
                    return True
                
        return False
        


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
solution = Solution()

print(solution.exist(board, "ABCCED"))
print(solution.exist(board, "SEE"))
print(solution.exist(board, "ABCB"))