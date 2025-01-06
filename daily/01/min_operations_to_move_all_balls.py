# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
# 6/1//24
""" 
    answer is the distance of the ith position from all
    other positions with '1'.

    Naive solution: For each i, iterate through the list and
    determine the total of the distance between itself and all boxes with '1'.

    Instead, notice that as we consider a box more rightward, the distance between the #
    of '1's on the right each decrease by 1. On the other hand, the distance between the # of
    '1's on the left increase by 1.

    Base case? In the first loop iteration, find the starting # of operations from the first node,
    and also the # of '1's on the RHS.
        We also need to account for the case where the starting box is a '1'. In this case, increment n_l by 1.



"""
def minOperations(boxes: str) -> list[int]:
    boxes = list(boxes)
    answer = []

    n_l = n_r = 0
    curr_operations = 0

    for (i, box) in enumerate(boxes[1:], start=1):
        if box == '1':
            n_r += 1
            curr_operations += i
    
    answer.append(curr_operations)

    if boxes[0] == '1':
        n_l += 1

    for box in boxes[1:]:
        curr_operations -= n_r
        curr_operations += n_l

        if box == '1':
            n_r -= 1
            n_l += 1

        answer.append(curr_operations)

    return answer

print(minOperations("110"))
print(minOperations("001011"))