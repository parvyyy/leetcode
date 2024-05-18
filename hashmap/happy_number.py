def isHappy(n: int) -> bool:

  # If you reach the same number again, it means that you are in a loop.
  visited_nums = set()

  while n != 1:
    if n in visited_nums:
      return False

    visited_nums.add(n)

    sq_sum = 0
    for digit in str(n):
      sq_sum += int(digit) ** 2

    n = sq_sum


  return True

print(isHappy(19))
print(isHappy(2))