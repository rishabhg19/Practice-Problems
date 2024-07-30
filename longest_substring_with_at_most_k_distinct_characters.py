# Leetcode 340
# Longest Substring with At Most K Distinct Characters
# Sliding window approach
from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        longest = 0
        freqs = Counter()
        left = 0

        for right in range(n):
            freqs[s[right]] += 1
            if len(freqs) <= k:
                longest = max(longest, right - left + 1)
            while len(freqs) > k:
                if freqs[s[left]] == 1:
                    del freqs[s[left]]
                else:
                    freqs[s[left]] -= 1
                left += 1
        return longest
        