# Problem: https://leetcode.com/problems/valid-sudoku/
# NeetCode 150 – Arrays & Hashing
# Difficulty: Medium
# Time: O(n^2), Space: O(n^2)

from typing import List
    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ### For varying board sizes
        # board_size = len(board)
        # block_col_count = int(sqrt(board_size))
        board_size = 9      # cell count along an axis
        block_col_count = 3 # block count along an axis
        b_sets = [set() for _ in range(board_size)]
        r_sets = [set() for _ in range(board_size)]
        c_sets = [set() for _ in range(board_size)]
        for r in range(0, board_size):
            r_vals = board[r]
            r_set = r_sets[r]
            for c in range(0, board_size):
                item = r_vals[c]
                if item == '.':
                    continue
                c_set = c_sets[c]
                block = (r // block_col_count) * block_col_count + (c // block_col_count)
                b_set = b_sets[block]
                if item in r_set or item in c_set or item in b_set:
                    return False
                r_sets[r].add(item)   
                c_sets[c].add(item)
                b_sets[block].add(item)
        return True
