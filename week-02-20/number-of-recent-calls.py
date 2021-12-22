class RecentCounter:
    timeline: List
    def __init__(self):
        self.timeline = []

    def ping(self, t: int) -> int:
        self.timeline.append(t)
        counter = 0
        for i in range(len(self.timeline) - 1, -1, -1):
            if self.timeline[i] < t - 3000:
                break
            counter  = counter + 1
        return counter


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)