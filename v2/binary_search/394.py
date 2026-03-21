from typing import List;
from collections import Counter

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1, nums2 = set(nums1), set(nums2)
    nums3 = set()

    for num in nums1:
        if num in nums2:
            nums3.add(num)

    return list(nums3)

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = Counter(nums1)
    nums2 = Counter(nums2)

    nums3 = []
    for k in nums1:
        n = min(nums1[k], nums2[k])
        nums3 = nums3 + (n * [k])

    return nums3

res = intersect([1,2,2,1], [2,2])
res = intersect([4,9,5], [9,4,9,8,4])
print(res)