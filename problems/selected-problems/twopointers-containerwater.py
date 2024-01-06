"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area


if __name__ == "__main__":
    solution = Solution()
    print(solution.max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
