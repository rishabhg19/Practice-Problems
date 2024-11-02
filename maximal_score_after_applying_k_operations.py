class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxheap = [-1 * num for num in nums[:]]
        heapq.heapify(maxheap)
        score = 0
        operations = 1
        while operations <= k:
            #print(maxheap)
            prevNum = heapq.heappop(maxheap)
            score += -1*prevNum
            heapq.heappush(maxheap, floor(prevNum/3))
            operations += 1
        return score