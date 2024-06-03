# Leetcode 567 Permutation in String
# Method sliding window using list to count
# frequencies of letters in small string
# comparing this to frequencies in big string
# using sliding window loop

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        counts1 = [0] * 26
        counts2 = [0] * 26

        for character in s1:
            counts1[ord(character)-ord('a')] += 1

        # sliding window loop
        for i in range(len2):
            counts2[ord(s2[i])-ord('a')] += 1
            if i >= len1:
                counts2[ord(s2[i-len1])-ord('a')] -= 1
            if counts1 == counts2:
                return True
        return False
        