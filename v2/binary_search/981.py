from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.map = defaultdict(lambda: list())

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    # Perform a binary search on the retrieved list,
    # where the `timestamp` is the `target` value
    def get(self, key: str, timestamp: int) -> str:
        ls = self.map[key]
        n = len(ls)

        if n == 0:
            return ""
        
        lo, hi = 0, n - 1

        if ls[lo][0] > timestamp:
            return ""
        
        if ls[hi][0] <= timestamp:
            return ls[hi][1]

        while lo + 1 < hi:
            mid = int((lo + hi) / 2)

            time, val = ls[mid]

            if time == timestamp:
                return val
            elif time < timestamp:
                lo = mid
            else:
                hi = mid
        
        # The lower term is always less than the timestamp.
        _, val = ls[lo]

        return val

timeMap = TimeMap();
timeMap.set("foo", "bar", 1); 
print(timeMap.get("foo", 1))        
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4);   
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))