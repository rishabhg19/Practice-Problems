# Leetcode 159
# Longest Substring with at most two distinct characters
# Sliding window

from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        left = 0

        # maxlen keeps track of the longest substring
        # with two distinct characters
        # freqs keeps track of the counts of each 
        # character in the substring of the current window
        maxlen = 0
        freqs = Counter()

        for right in range(n):
            # add the rightmost character and increment 
            # its count
            freqs[s[right]] += 1

            # if there are over two distinct characters
            # shrink window from the left and
            # update freqs accordingly
            while len(freqs) > 2:
                if freqs[s[left]] == 1:
                    del freqs[s[left]]
                else:
                    freqs[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen