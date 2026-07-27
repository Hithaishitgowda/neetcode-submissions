class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      hashmap = {}
      l = []
      for i in nums:
        hashmap[i] = 1 + hashmap.get(i, 0)
      sss = sorted(hashmap.items(), key = lambda x : x[1], reverse= True)
      for j in range(k):
        l.append(sss[j][0])
      return l
      