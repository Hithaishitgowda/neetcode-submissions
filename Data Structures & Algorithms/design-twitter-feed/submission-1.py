import heapq
class Twitter:

    def __init__(self):
        self.heap = []
        self.time = 0
        self.hashset = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.heap, (-self.time, userId, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        heap2 = self.heap.copy()
        output = []
        while heap2 and len(output) < 10:
            ttime, Tweet_userId, Tweet_tweetId = heapq.heappop(heap2)

            if (Tweet_userId == userId) or (Tweet_userId in self.hashset.get(userId, set())):
                output.append(Tweet_tweetId)
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hashset:
            self.hashset[followerId] = set()
        
        self.hashset[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.hashset:
            self.hashset[followerId].discard(followeeId)
        
