class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_true = 0 
        column_true = 0
        box_true = 0
        n = len(board)

        # rows
        for row in board:
            sub_row = []
            for number in row:
                if number != ".":
                    sub_row.append(number)

            if len(set(sub_row)) == len(sub_row):
                row_true += 1


        # column
        for column in range(n):
            sub_column = []
            for number in range(n):
                if board[number][column] != ".":
                    sub_column.append(board[number][column])

            if len(set(sub_column)) == len(sub_column):
                column_true += 1


        # box
        for big_start in range(0, 9, 3):
            for start in range(0, 9, 3):
                box = []
                for x in range(start, start + 3):
                    for y in range(big_start, big_start + 3):
                        if board[x][y] != ".":
                            box.append(board[x][y])
                
                if len(set(box)) == len(box):
                    box_true += 1

        if row_true == column_true == box_true == 9:
            return True
        return False
                  

'''
0 012  345  678
1 
2 

3 012  345  678
4
5

6 012  345  678
7
8
'''    


solution = Solution()
print(solution.isValidSudoku([
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(solution.isValidSudoku([
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))