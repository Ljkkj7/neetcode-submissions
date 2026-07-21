class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square = self.solve3x3(board)
        row = self.solverow(board)
        col = self.solvecol(board)

        if square and row and col:
            return True
        else:
            return False
    
    def solvecol(self, board):
        for i in range(len(board)):
            check = set()
            for j in range(len(board)):
                if board[j][i] not in check:
                    if board[j][i] != '.':
                        check.add(board[j][i])
                else:
                    return False
        return True

    def solverow(self, board):
        for i in board:
            check = set()
            for j in i:
                if j not in check:
                    if j != '.':
                        check.add(j)
                else:
                    return False
        return True
        

    def solve3x3(self, board):
        y_index = 0
        x_index = 0

        chunker = 3

        while y_index < len(board):
            check = set()

            for i in range(y_index, y_index+chunker):
                for j in range(x_index, x_index+chunker):
                    if board[i][j] in check:
                        if board[i][j] != '.':
                            return False
                    check.add(board[i][j])

            if x_index == 6:
                x_index = 0
                if y_index == 6:
                    return True
                else:
                    y_index += chunker
            else:
                x_index += chunker
                
            

