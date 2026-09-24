class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = set()
        row = set()
        for i in board:
            for j in i:
                if j!=".":
                    if j not in row:
                        row.add(j)
                    else:
                        print(1)
                        return False
            row = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] not in column:
                        column.add(board[j][i])
                    else:
                        print(2)
                        return False
            column = set()
        boxes = [set() for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] not in boxes[(i//3)*3+j//3]: 
                        boxes[(i//3)*3+j//3].add(board[i][j])
                    else:
                        print(boxes)
                        return False
        return True