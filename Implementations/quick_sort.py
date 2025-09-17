# Implementation of quick sort (unstable, in-place)
# Time complexity: O(n log(n)) or O(n^2) if sorted
# Space complexity: O(log(n))

from typing import List


def quickSort(arr: List[int]) -> List[int]:
    def partition(arr: List[int], start: int, end: int) -> int:
        pivot = arr[end]
        i = start
        j = start - 1
        
        while i != end:
            if arr[i] < pivot:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
        
        j += 1
        arr[end], arr[j] = arr[j], arr[end]
        
        return j
            
    def sort(arr: List[int], start: int, end: int) -> List[int]:
        if end <= start:
            return arr
        
        pivot = partition(arr, start, end)
        sort(arr, start, pivot - 1)
        sort(arr, pivot + 1, end)
        return arr
        
    return sort(arr, 0, len(arr) - 1)
