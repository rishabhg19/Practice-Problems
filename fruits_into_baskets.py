# Leetcode 904 Fruits into Baskets
# Sliding window

from collections import Counter
class Solution:
    # TRICK - reframe the problem as find the longest
    # subarray with no more than TWO distinct elements
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)

        # basket keeps track of each distinct element and it's count
        # maxval counts the total of number of fruits
        # each distinct element is a fruit
        basket = Counter()
        left = 0
        maxval = 0
        for right in range(n):
            # add a fruit from the current tree
            # tree is just position/index
            basket[fruits[right]] += 1

            # while basket has more than 2 fruits
            # remove the fruit from the leftmost tree
            while len(basket) > 2:
                if basket[fruits[left]] == 1:
                    del basket[fruits[left]]
                else:
                    basket[fruits[left]] -= 1
                left += 1
            # record the maxval
            maxval  = max(maxval, sum(basket.values()))
        return maxval

        