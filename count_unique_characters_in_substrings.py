# Leetcode 828 
# Count Unique Characters of All Substrings of a Given String

from collections import Counter
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # get a dictionary with keys as unique characters in s
        # could use a set here as well
        sCounts = Counter(s)

        # start building dictionary mapping unique
        # characters in the input
        # to the indices where they occur
        # prepend each list with -1
        # append each list with len(input)
        unique_indices = defaultdict(list)
        for key in sCounts:
            unique_indices[key].append(-1)
            for i in range(len(s)):
                if key == s[i]:
                    unique_indices[key].append(i)
        for key in unique_indices:
            unique_indices[key].append(len(s))
        result = 0

        # calculate the cross product
        for key in unique_indices:
            for i in range(1, len(unique_indices[key])-1):
                result += (unique_indices[key][i] - unique_indices[key][i-1]) * (unique_indices[key][i+1] - unique_indices[key][i]) 
        print(unique_indices)
        return result
        