class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        a = intervals[0][0]
        b = intervals[0][1]
        for x,y in intervals:
            if x <= b:
                b = max(b,y)
            else:
                output.append([a,b])
                a = x
                b = y

        output.append([a,b])

        return output
            