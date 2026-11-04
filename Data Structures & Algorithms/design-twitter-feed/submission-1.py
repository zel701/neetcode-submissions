class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.time,tweetId])
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for i in self.tweets[userId]:
            heapq.heappush(heap,i)
        for i in self.following[userId]:
            for j in self.tweets[i]:
                heapq.heappush(heap,j)
        res = []
        while heap and len(res)<10:
            res.append(heapq.heappop(heap)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!= followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
