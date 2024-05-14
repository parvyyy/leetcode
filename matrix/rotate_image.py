# Flip fhe matrix across the y-axis.
# Then, Flip the matrix diagonally.
def swap(matrix, x, y):
  tmp = matrix[x[0]][x[1]]
  matrix[x[0]][x[1]] = matrix[y[0]][y[1]]
  matrix[y[0]][y[1]] = tmp
  return

def rotate(matrix):
  n = len(matrix)

  for i in range(n):
    # Flips the matrix across the y-axis.
    # ALTERNATIVE: Reverse each row (i.e. matrix[i] = matrix[i][::-1])
    for j in range(n // 2):
      swap(matrix, (i, j), (i, n - j - 1))
  
  for i in range(n):
    for j in range(n - i):
      # This is a transposition of the matrix but from the bottom left to top right.
      swap(matrix, (i, j), (n - 1 - j, n - 1 - i))

  return

rotate([[1,2,3],[4,5,6],[7,8,9]])
rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])