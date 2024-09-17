class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        currMax = min(height[right],height[left]) * (right - left)

        while left <= right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            currMax = max(currMax, min(height[right],height[left]) * (right - left ))
        return currMax
        