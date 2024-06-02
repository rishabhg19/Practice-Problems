# Leetcode 643 Maximum Average Subarray
# Cumulative sum approach

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # HANDLE EDGE CASES
        if n == 1:
            return nums[0]
        if n == k:
            return sum(nums) / k
        # MAKE SURE THE FIRST ELEMENT IN SUMS IS THE FIRST ELEMENT
        # IN THE INPUT LIST
        sums = [nums[0]] * n
        for i in range(1,n):
            sums[i] = sums[i-1] + nums[i]
        print(sums)
        result = sums[k-1] / k
        for i in range(k,n):
            result = max(result, (sums[i] - sums[i-k])/k)
        return result