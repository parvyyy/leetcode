def setZeroes(matrix):
    # O(m + n) space complexity
    rows = []
    cols = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    
    for j in range(len(matrix[0])):
        for row in rows:
            matrix[row][j] = 0

    for i in range(len(matrix)):
        for col in cols:
            matrix[i][col] = 0

    # To achieve O(1) time complexity, use the matrix's first row & col
    # to store the rows & cols that need to be set.
    