class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time+=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        users = []
        for i in self.following[userId]:
            users.append(i)
        users.append(userId)
        for user in users:
            if self.tweets[user]:
                index = len(self.tweets[user])-1
                time,tweetId = self.tweets[user][index][0],self.tweets[user][index][1]
                heapq.heappush(heap,(-time,tweetId,user,index))
        while heap and len(res)<10:
            time,tweetId,user,index = heapq.heappop(heap)
            res.append(tweetId)
            if index > 0:
                index -=1
                new_tweet = self.tweets[user][index]
                newTime,newId = new_tweet[0],new_tweet[1]
                heapq.heappush(heap,(-newTime,newId,user,index))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!= followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
