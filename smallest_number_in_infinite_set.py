class SmallestInfiniteSet:

    def __init__(self):
        self.set = [i for i in range(1, 10000)]
        

    def popSmallest(self) -> int:
        get_smallest = heapq.heapify(self.set)
        if self.set:
            return heapq.heappop(self.set)
        else:
            return 1
        

    def addBack(self, num: int) -> None:
        if num not in self.set:
            heapq.heappush(self.set, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)