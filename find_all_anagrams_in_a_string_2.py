# Leetcode 438 Find All Anagrams in a String
# Sliding window with list to count character frequency method

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen, plen = len(s), len(p)
        result = []
        pCounts = [0]*26
        sCounts = [0]*26
        for character in p:
            # ord(char) gets the alphabetical order value for indexing 
            # a is 0 b is 1 z is 25
            pCounts[ord(character) - ord('a')] += 1
        
        for i in range(slen):
            sCounts[ord(s[i])-ord('a')] += 1

            #window of length plen starts at index i-plen+1
            if i >= plen:
                sCounts[ord(s[i-plen])-ord('a')] -= 1
            
            if sCounts == pCounts:
                result.append(i-plen+1)
        return result
