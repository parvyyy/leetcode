def max_profit(prices):
  # Initial conditions - start: 0, size: 1
  i = 0; j = 0; max_prof = 0;

  # Terminating condition: 
  while (j < len(prices)):
    # If the current price (at idx i) is greater than a price (at idx j), where i < j,
    # Then, the difference of a price between will always be greater than the difference of
    # a price with i.
    if prices[i] >= prices[j]:
      i = j;
      j = j + 1
    # Otherwise, determine the difference, setting it as the max_prof if necessary & continue
    # increasing the window-size.
    else:
      max_prof = max(max_prof, prices[j] - prices[i]);
      j = j + 1;

  return max_prof;

assert max_profit([7,1,5,3,6,4]) == 5
assert max_profit([7,6,4,3,1]) == 0