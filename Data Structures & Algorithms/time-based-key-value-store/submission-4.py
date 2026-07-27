
class TimeMap:

    def __init__(self):
        self.dicti = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dicti:
            self.dicti[key] = []
        
        self.dicti[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dicti:
            return ""
        
        left = 0 
        right = len(self.dicti[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            if timestamp == self.dicti[key][mid][1]:
                return self.dicti[key][mid][0]

            elif timestamp > self.dicti[key][mid][1]:
                left = mid + 1

            else:
                right = mid - 1
        if right >= 0:
            return self.dicti[key][right][0]
        else:
            return ""
        return self.dicti[key][mid][0]