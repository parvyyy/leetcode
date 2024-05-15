def num_adjacent_alive_cells(matrix, i, j):
  return is_cell_alive(matrix, i - 1, j) + is_cell_alive(matrix, i + 1, j) + is_cell_alive(matrix, i, j - 1) + is_cell_alive(matrix, i, j + 1) + is_cell_alive(matrix, i - 1, j - 1) + is_cell_alive(matrix, i - 1, j + 1) + is_cell_alive(matrix, i + 1, j - 1) + is_cell_alive(matrix, i + 1, j + 1)

def is_cell_alive(matrix, i, j):
  if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
    return False
  
  return True if matrix[i][j] == 1 else False

def determine_cell(board, adjacency_board, i, j):
  if is_cell_alive(board, i, j):
    if adjacency_board[i][j] < 2: # Under population
      return 0
    elif adjacency_board[i][j] > 3: # Over population
      return 0
    else:
      return 1
  else: 
    if adjacency_board[i][j] == 3: # Reproduction
      return 1
    else:
      return 0

def gameOfLife(board):
  m, n = len(board), len(board[0])

  # Empty 2D (m x n) matrix
  adjacency_board = [[0 for j in range(n)] for i in range(m)];

  for i in range(m):
    for j in range(n):
      adjacency_board[i][j] = num_adjacent_alive_cells(board, i, j)

  for i in range(m):
    for j in range(n):
      board[i][j] = determine_cell(board, adjacency_board, i, j)

  return


gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
