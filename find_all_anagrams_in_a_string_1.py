from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen, plen = len(s), len(p)
        if slen < plen:
            return []

        # Counter(p) creates a map from each character
        # in string p to its frequency
        pCounts = Counter(p)
        sCounts = Counter()

        result = []

        for i in range(slen):
            # populating sCounts
            sCounts[s[i]] += 1

            # window starts moving here
            # because the window is of length plen
            # current window is [i - plen + 1, i]
            if i >= plen:
                # if there is only one of the letter 
                # in the map, delete it
                if sCounts[s[i - plen]] == 1:
                    del sCounts[s[i - plen]]
                # if there is more than one of the letter
                # decrease it by one since the window passed it
                else:
                    sCounts[s[i - plen]] -= 1
            # get the starting index of the window
            # when the anagram is detected
            if pCounts == sCounts:
                result.append(i - plen + 1)
        return result