import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = []

        time = 0

        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        for task, priority in count.items():
            heapq.heappush(heap, (-priority, task))

        while heap or queue:
            time += 1
            if queue and queue[0][2] == time:
                priority, task, _ = queue.pop(0)
                heapq.heappush(heap, (priority, task))

            if heap:
                priority, task = heapq.heappop(heap)
                priority += 1

                if priority < 0:
                    queue.append((priority, task, time+n+1))

        return time

        


        

        
