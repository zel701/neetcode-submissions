class Solution:
    def solve(self, board: List[List[str]]) -> None:
        unvisited = []
        h = len(board)
        w = len(board[0])
        visited =set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(w):
            if board[0][i] == 'O':
                unvisited.append((0,i))
                board[0][i] = "M"
            if board[h-1][i] == "O":
                unvisited.append((h-1,i))
                board[h-1][i] = "M"
        for j in range(0,h):
            if board[j][0] == "O":
                unvisited.append((j,0))
                board[j][0] = "M"
            if board[j][w-1] == "O":
                unvisited.append((j,w-1))
                board[j][w-1] = "M"
        for i in unvisited:
            visited.add(i)
        while unvisited:
            current = []
            for y,x in directions:
                for j,k in unvisited:
                    if 0 <=y+j < h and 0<= x+k < w and board[y+j][x+k] == "O" and (y+j,x+k) not in visited:
                        board[y+j][x+k] = "M"
                        current.append((y+j,x+k))
                        visited.add((y+j,x+k))
            unvisited = current.copy()
        for i in range(h):
            for j in range(w):
                if board[i][j] == "M":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"