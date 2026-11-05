class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        current = self.values[key]
        left = 0
        right = len(current)-1
        if not current:
            return ""
        if timestamp<current[0][0]:
            return ""
        if len(current) == 1:
            return current[0][1]
        mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            if current[mid][0] == timestamp:
                return current[mid][1]
            if current[mid][0] > timestamp:
                right = mid-1
            else:
                left = mid+1
        if current[mid][0]<timestamp:
            return current[mid][1]
        else:
            return current[mid-1][1]


        
        
