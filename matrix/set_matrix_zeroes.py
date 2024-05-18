def setZeroes(matrix):
  n, m = len(matrix), len(matrix[0])

  # A set is preferred to avoid iterating through already set rows/cols.
  rows = set()
  cols = set()

  for i in range(n):
      for j in range(m):
          if matrix[i][j] == 0:
              rows.add(i)
              cols.add(j)

  # Set entire row to zero
  for j in range(m):
      for row in rows:
          matrix[row][j] = 0

  # Set entire col to zero
  for i in range(n):
      for col in cols:
          matrix[i][col] = 0
  
  return