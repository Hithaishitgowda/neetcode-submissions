class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        for src, dst in tickets:
            if src not in graph:
                graph[src] = []

            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse=True)

        result = []

        def dfs(src):
            while src in graph and graph[src]:
                dst = graph[src].pop()
                dfs(dst)

            result.append(src)

        dfs("JFK")

        return result[::-1]