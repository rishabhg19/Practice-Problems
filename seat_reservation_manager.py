class SeatManager:

    def __init__(self, n: int):
        self.seats = [[False, i+1] for i in range(n)]

    def reserve(self) -> int:
        #priority = heapq.heapify(self.seats)
        reservation = [True, heapq.heappop(self.seats)[1]]
        heapq.heappush(self.seats, reservation)
        return reservation[1]
        

    def unreserve(self, seatNumber: int) -> None:
        # for seat in self.seats:
        #     if seat[1] == seatNumber:
        #         seat[0] = False
        heapq.heappush(self.seats, [False, seatNumber])


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)