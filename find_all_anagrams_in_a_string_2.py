class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen, plen = len(s), len(p)
        result = []
        pCounts = [0]*26
        sCounts = [0]*26
        for character in p:
            pCounts[ord(character) - ord('a')] += 1
        
        for i in range(slen):
            sCounts[ord(s[i])-ord('a')] += 1

            #window of length plen starts at index i-plen+1
            if i >= plen:
                sCounts[ord(s[i-plen])-ord('a')] -= 1
            
            if sCounts == pCounts:
                result.append(i-plen+1)
        return result