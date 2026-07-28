class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}

        for word in words:
            for char in word:
                graph[char] = set()

        indegree = {char: 0 for char in graph}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            length = min(len(word1), len(word2))

            if word1[:length] == word2[:length] and len(word1) > len(word2):
                return ""

            for j in range(length):
                if word1[j] != word2[j]:

                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1

                    break

        from collections import deque

        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

        if len(result) != len(graph):
            return ""

        return "".join(result)