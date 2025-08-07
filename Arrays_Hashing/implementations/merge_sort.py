# Implementation of merge sort
# Time complexity: O(n log n)
# Space complexity: O(n)

from typing import List

def merge(left: List[int], right: List[int]) -> List[int] :
    lPt, rPt = 0, 0
    arr = []
    while lPt != len(left) and rPt != len(right):
        if left[lPt] <= right[rPt]:
            arr.append(left[lPt])
            lPt += 1
        else:
            arr.append(right[rPt])
            rPt += 1
            
    arr.extend(left[lPt:] + right[rPt:])
    return arr
            
def mergeSort(arr: List[int]) -> List[int]:
    m = len(arr) // 2
    if m != 0:
        left = mergeSort(arr[:m])
        right = mergeSort(arr[m:])
        arr = merge(left, right)
    
    return arr
