# Implementation of count sort (stable, best for when range is less than length)
# Time complexity: O(n + k) where n is the length of the array, and k is the range of values
# Space complexity: O(n + k)

from typing import List

def countSort(arr: List[int]) -> List[int]:
    min_val, max_val = min(arr), max(arr)
    range_val = max_val - min_val + 1
    
    freq_arr = [0] * range_val
    for n in arr:
        freq_arr[n - min_val] += 1
    
    for i in range (1, len(freq_arr)):
        freq_arr[i] += freq_arr[i - 1]    

    res = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        freq = freq_arr[num - min_val]
        res[freq - 1] = num
        freq_arr[num - min_val] -= 1
        
    return res
