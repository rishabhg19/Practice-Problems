from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqs = Counter()
        for num in nums:
            freqs[num] += 1
        for num in freqs:
            if freqs[num] > 1:
                return True
        return False