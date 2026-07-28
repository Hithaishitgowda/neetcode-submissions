import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortedQueries = sorted(queries)

        heap = []
        result = {}
        i = 0

        for q in sortedQueries:

            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r - l + 1

                heapq.heappush(heap, (size, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                result[q] = heap[0][0]
            else:
                result[q] = -1

        return [result[q] for q in queries]