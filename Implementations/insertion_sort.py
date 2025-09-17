# Implementation of insertion sort
# Time complexity: O(n^2)
# Space complexity: O(1)

from typing import List


def insertionSort(arr: List[int]) -> List[int]:
    count = len(arr)
    if count <= 1:
        return arr
    
    for i in range(1, count):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    return arr
