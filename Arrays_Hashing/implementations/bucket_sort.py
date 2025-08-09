# Implementation of bucket sort
# Time complexity: O(n^2) - degraded by quickSort
# Space complexity: O(n)

from typing import List
from quick_sort import quickSort


def bucketSort(arr: List[int], bucket_count: int = 10) -> List[int]:
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_width = max(1, (max_val - min_val) / bucket_count)
    buckets = [[] for _ in range(bucket_count)]
    
    for n in arr:
        index = min(bucket_count - 1, int((n - min_val) // bucket_width))
        buckets[index].append(n)
    
    sorted_arr = []
    for bucket in buckets:
        bucket = quickSort(bucket)
        sorted_arr.extend(bucket)
        
    return sorted_arr
