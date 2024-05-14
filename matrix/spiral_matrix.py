from typing import List
from enum import Enum

class Direction(Enum):
  RIGHT = 1
  DOWN = 2
  LEFT = 3
  UP = 4


def isOutOfBounds(matrix, i, j):
  return i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0])

def isTraversed(traversed, i, j):
  return (i, j) in traversed

def isSurrounded(matrix, traversed, i, j):
  return (isOutOfBounds(matrix, i - 1, j) or isTraversed(traversed, i - 1, j)) and (isOutOfBounds(matrix, i, j - 1) or isTraversed(traversed, i, j - 1)) and (isOutOfBounds(matrix, i + 1, j) or isTraversed(traversed, i + 1, j)) and (isOutOfBounds(matrix, i, j + 1) or isTraversed(traversed, i, j + 1))

def spiralOrder(matrix: List[List[int]]):
  # Mark all squares that have been travelled on.

  # Set a direction as RIGHT, LEFT, UP, DOWN
    # If the next element in the direction is marked or out of bounds. Go to next direction.
    # Else continue traversing in the selected direction - marking squares.
  
  traversed = set()
  spiral_order = []

  direction = Direction.RIGHT
  i, j = 0, -1

  while not isSurrounded(matrix, traversed, i, j):
    if direction is Direction.RIGHT:
      j += 1

      while not isOutOfBounds(matrix, i, j) and (i, j) not in traversed:
        traversed.add((i, j))
        spiral_order.append(matrix[i][j])

        j += 1

      
      direction = Direction.DOWN
      j -= 1 # Correction due to exceeding bounds
      
    elif direction is Direction.DOWN:
      i += 1

      while not isOutOfBounds(matrix, i, j) and (i, j) not in traversed:
        traversed.add((i, j))
        spiral_order.append(matrix[i][j])

        i += 1
      
      
      
      direction = Direction.LEFT
      i -= 1 # Correction due to exceeding bounds

    elif direction is Direction.LEFT:
      j -= 1

      while not isOutOfBounds(matrix, i, j) and (i, j) not in traversed:
        traversed.add((i, j))
        spiral_order.append(matrix[i][j])

        j -= 1

      
      
      direction = Direction.UP
      j += 1 # Correction due to exceeding bounds

    elif direction is Direction.UP:
      i -= 1

      while not isOutOfBounds(matrix, i, j) and (i, j) not in traversed:
        traversed.add((i, j))
        spiral_order.append(matrix[i][j])

        i -= 1

      
      direction = Direction.RIGHT
      i += 1 # Correction due to exceeding bounds
      
    else:
      break

  return spiral_order

print(spiralOrder([[1]])) # 1
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # 1 2 3 4 8 12 11 10 9 5 6 7
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # 1 2 3 6 9 8 7 4 5