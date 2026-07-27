class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in strs:
            h1 = {}

            for j in i:
                h1[j] = 1 + h1.get(j, 0)

            key = tuple(sorted(h1.items()))

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(i)

        return list(hashmap.values())