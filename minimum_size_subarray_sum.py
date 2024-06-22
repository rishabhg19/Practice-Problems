# Leetcode 209 Minimum Size Subarray Sum
# Sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if max(nums) >= target:
            return 1
        n = len(nums)
        minlen = 0
        l = 0
        r = 0
        currSum = 0
        # minlen is the answer
        # initialize it to infinity to begin with
        minlen = float("inf")

        # grow window to the right
        for r in range(n):
            # compute the current sum
            currSum += nums[r]

            # contract window when the sum is valid
            # until it is invalid again
            while currSum >= target:
                # record the answer of the previous valid sum
                minlen = min(minlen, r - l + 1)
                currSum -= nums[l]
                l += 1

        # return 0 if there was no valid answer
        if minlen == float("inf"):
            return 0
        else:
            return minlen
        