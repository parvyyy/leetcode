A new directory focused on preparation for Grad roles.

The focus will be on approaching key topics and mastering them.

General
 - Read entire question before writing, walk through each provided test case.
 - Write out any special properties / observations

Topic #1: Binary Search
 - Found that `while lo + 1 < hi` works well.
 - Consider whether it is appropriate to round `mid` down or up.
    - If no clear choice, round down & explain the consequences w/ `lo`.
 - Consider the final values of `lo` & `hi`.
    - Is another iteration required to find the suitable one to return,
      or is one of them already suitable.
 - Consider edge cases
    - Where `hi = lo` immediately.

Topic #2: Linked Lists
 - Works well to `curr = head` (and `prev = None`).
 - When initialising the `head` is conditional, make it a dummy ListNode
   and return `head.next` instead.