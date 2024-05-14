from typing import List

def getBoxNum(i, j):
  if i >= 0 and i < 3 and j >= 0 and j < 3:
    return 1
  if i >= 0 and i < 3 and j >= 3 and j < 6:
    return 2
  if i >= 0 and i < 3 and j >= 6 and j < 9:
    return 3
  if i >= 3 and i < 6 and j >= 0 and j < 3:
    return 4
  if i >= 3 and i < 6 and j >= 3 and j < 6:
    return 5
  if i >= 3 and i < 6 and j >= 6 and j < 9:
    return 6
  if i >= 6 and i < 9 and j >= 0 and j < 3:
    return 7
  if i >= 6 and i < 9 and j >= 3 and j < 6:
    return 8
  if i >= 6 and i < 9 and j >= 6 and j < 9:
    return 9
  
def isValidSudoku(board: List[List[str]]):
  row = set()
  col = set()
  box = set()

  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == '.':
        continue

      if (i, board[i][j]) in row or (j, board[i][j]) in col or (getBoxNum(i, j), board[i][j]) in box:
        return False

      row.add((i, board[i][j]))
      col.add((j, board[i][j]))
      box.add((getBoxNum(i, j), board[i][j]))

  return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))