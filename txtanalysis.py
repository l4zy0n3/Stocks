from textblob import TextBlob
import tweepy
import datetime

class TweetSentiments:
    
    def __init__( self):
        self.consumer_key = 'PoQKNomy0kbwHzQojjN8zLc6n'
        self.consumer_secret = 'DnXGSnCPxDkXeQoyU0DgE7EFqalV8NMmvFt9rDYTGUhoKTmwg6'
        self.access_token = '2741354322-pMH48FBZutbWGaYP4nO1sb8xWFbVCPfe23QUHeu'
        self.access_token_secret = 'qcahLI7f1qVDbPboJOngHHasN7wCZaQ6bODkBtR8BHpLP' #put your own
        self.auth = tweepy.OAuthHandler( self.consumer_key, self.consumer_secret)
        self.auth.set_access_token( self.access_token, self.access_token_secret)
        self.api = tweepy.API( self.auth)

    def get_input( self, input_string, tweet_date):
        self.overall = 0
        self.count_not_zero = 0
        self.list_tweets = []
        self.tweet_date = datetime.datetime.strptime( tweet_date+'-00-00', "%Y-%m-%d-%H-%M").date()
        self.tweets = self.api.search\
        ( input_string, since = self.tweet_date, until = (self.tweet_date + datetime.timedelta( days = 1)))
        for tweet in self.tweets:
            if tweet.lang == "en":
                self.list_tweets.append(tweet.text)
        return self.calculate()

    def calculate( self):
        for tweet in self.list_tweets:
            blob = TextBlob(tweet)   
            print(tweet)
            print(self.tweet_date)
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
            print(self.count_not_zero)
            self.overall/=self.count_not_zero
            return self.overall
#print(overall,"Overall..." if overall>0.0 else( "Neutral..." if overall == 0.0 else "Negative..."))