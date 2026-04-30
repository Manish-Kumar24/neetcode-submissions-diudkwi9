class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)   # user → [(time, tweetId)]
        self.followMap = defaultdict(set)   # user → set(followees)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):
        res = []
        maxHeap = []

        # user should follow himself
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]

                # push: (-time, tweetId, userId, index)
                heapq.heappush(maxHeap, (-time, tweetId, followee, idx - 1))

        while maxHeap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(maxHeap)
            res.append(tweetId)

            if idx >= 0:
                time, tweetId = self.tweetMap[user][idx]
                heapq.heappush(maxHeap, (-time, tweetId, user, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)