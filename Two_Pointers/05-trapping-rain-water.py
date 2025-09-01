# Problem: https://leetcode.com/problems/trapping-rain-water/
# NeetCode 150 – Two Pointers
# Difficulty: Easy/Medium/Hard
# Time: O(), Space: O()

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        i = 0
        while i < len(height) - 1:
            if height[i] == 0:
                i += 1
                continue

            cur_wall = height[i]
            j = i + 1
            max_wall = (j, 0)

            while j < len(height) and height[j] < cur_wall:
                if height[j] > max_wall[1]:
                    max_wall = (j, height[j])
                j += 1

            if j < len(height):
                wall_idx = j
                wall_height = height[j]
            else:
                wall_idx = max_wall[0]
                wall_height = max_wall[1]
				
            min_height = min(cur_wall, wall_height)
            for k in range(i + 1, wall_idx):
                total_area += max(0, min_height - height[k])

            i = wall_idx  # Move to next wall

        return total_area


ls = [0,1,0,2,1,0,1,3,2,1,2,1]
o = Solution()
o.trap
