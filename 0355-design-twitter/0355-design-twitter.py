class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(dict)
        self.count = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId][tweetId] = self.count
        self.count += 1
        # print(f"posted tweet. New tweets: {self.tweets}")

    def getNewsFeed(self, userId: int) -> List[int]:
        relevantTweets = []
        for user in self.following[userId] | {userId}:
            relevantTweets.extend((count, tweetId) for tweetId, count in list(self.tweets[user].items())[-10:])
        relevantTweets.sort(reverse=True)
        # print(f"relevantTweets: {relevantTweets}")
        return [tweetId for (_, tweetId) in relevantTweets[:10]]
                                  
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)