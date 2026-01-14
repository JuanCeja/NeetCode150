# 
# 
# 
# 
# 
# 
# 


class TimeMap:

    def __init__(self):
        self.store = {
            self.key = (self.value, self.timestamp)
        }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
    

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1

        while l < r:
            mid = (l + r) // 2
            mid_value = self.store[key][-1]

            if mid_value == timestamp:
                return self.store[key][0]

            if mid_value < timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return 