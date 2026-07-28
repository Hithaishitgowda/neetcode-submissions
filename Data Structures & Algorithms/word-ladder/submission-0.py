from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            word, count = queue.popleft()

            if word == endWord:
                return count

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + char + word[i + 1:]

                    if newWord in words and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, count + 1))

        return 0       