class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        res = ""
        store_list = self.store[key]
        l, r = 0, len(store_list) - 1

        while l <= r:
            mid = (l + r) // 2

            if store_list[mid][0] == timestamp:
                return store_list[mid][0]

            if store_list[mid][0] > timestamp:
                r = mid - 1
            else:
                res = store_list[mid][0]
                l = mid + 1

        return res