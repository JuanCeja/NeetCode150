class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))
    

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1
        closest = 0

        while l <= r:
            mid = (l + r) // 2
            mid_timestamp = self.store[key][mid][-1]

            if mid_timestamp == timestamp:
                return self.store[key][mid][0]

            if mid_timestamp <= timestamp:
                closest = max(closest, mid)
                l = mid + 1
            else:
                r = mid - 1


        return self.store[key][closest][0]