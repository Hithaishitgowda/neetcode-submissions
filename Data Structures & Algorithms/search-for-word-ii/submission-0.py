class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root

            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()

                curr = curr.children[c]

            curr.word = word

        rows = len(board)
        cols = len(board[0])

        result = []

        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            char = board[r][c]

            if char == "#" or char not in node.children:
                return

            nextNode = node.children[char]

            if nextNode.word:
                result.append(nextNode.word)
                nextNode.word = None

            board[r][c] = "#"

            dfs(r + 1, c, nextNode)
            dfs(r - 1, c, nextNode)
            dfs(r, c + 1, nextNode)
            dfs(r, c - 1, nextNode)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result