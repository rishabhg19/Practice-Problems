class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        currSum = sum(nums[:k])
        result = currSum
        # WINDOW IS OF LENGTH K
        # nums[i-k] is what got slid past
        # nums[i] is newly slid on
        for i in range(k, n):
            currSum += nums[i] - nums[i-k]
            result = max(result, currSum)
        return result / k