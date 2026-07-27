import heapq
import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        heap = []
        for x, y in points:
            dis = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap, (dis, [x,y]))

        for _ in range(k):
            dis, point = heapq.heappop(heap)
            output.append(point)

        return output 

        