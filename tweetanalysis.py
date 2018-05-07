import got3 as got
from textblob import TextBlob
import datetime

class TweetSentiments:
    
    def __init__( self, input_string, tweet_date):
        self.overall = 0
        self.input_string = input_string
        self.count_not_zero = 0
        self.list_tweets = []
        self.tweet_date = tweet_date

    def calculate( self):
        tweet_criteria = got.manager.TweetCriteria()\
        .setQuerySearch( '#'+self.input_string).setUntil\
        ( self.tweet_date).setTopTweets(True).setMaxTweets(10)
        self.tweets = got.manager.TweetManager.getTweets(tweet_criteria)
        for tweet in self.tweets:
            self.list_tweets.append(tweet.text)
        for tweet in self.list_tweets:
            blob = TextBlob(tweet) 
            avg = 0
            for sentence in blob.sentences:
                avg += sentence.sentiment.polarity
            avg /= len(blob.sentences)
            if avg != 0.0:
                self.overall += avg
                self.count_not_zero += 1
            # print( avg, "Positive..." if avg>0.0 else( "Neutral..." if avg == 0.0 else "Negative...") )

        if self.count_not_zero == 0:
            return 0.0
        else:
            self.overall/=self.count_not_zero
            print(self.overall)
            return self.overall