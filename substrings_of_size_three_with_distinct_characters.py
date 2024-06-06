# Leetcode 1876 
# Substrings of Size Three with Distinct Characters
# Sliding window

from collections import Counter
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        currWindow = Counter(s[:3])
        count = 0
        if len(currWindow) == 3:
            count += 1
        for i in range(3,n):
            currWindow[s[i]] += 1
            if currWindow[s[i-3]] == 1:
                del currWindow[s[i-3]]
            else:
                currWindow[s[i-3]] -= 1
            if len(currWindow) == 3:
                count += 1
        return count

        