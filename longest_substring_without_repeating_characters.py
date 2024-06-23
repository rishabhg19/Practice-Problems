# Leetcode 3 Longest Substring Without Repeating Characters
# Sliding window
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty string return 0
        if s == "":
            return 0
        left = 0
        n = len(s)
        currCounts = Counter()
        # the max nonrepeating substring is 1 so far
        maxlen = 1

        # expand window to the right
        for right in range(n):
            # update frequency counter with current window
            currCounts[s[right]] += 1
            # update the maxlength as soon as new character is counted
            maxlen = max(maxlen, len(currCounts))

            # if a character becomes nonunique, shrink window
            # it is unique again
            # NOTE - maxlen cannot be updated inside the while
            # loop because one of the elements might get removed
            # from the left side of the window and the maxlen
            # is determined from the length of currCounts
            while currCounts[s[right]] > 1:
                if currCounts[s[left]] == 1:
                    del currCounts[s[left]]
                else:
                    currCounts[s[left]] -= 1
                left += 1
        return maxlen



        