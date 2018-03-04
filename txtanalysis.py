from textblob import TextBlob
import tweepy as tw

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = '' #put your own

auth = tw.OAuthHandler( consumer_key, consumer_secret)
auth.set_access_token( access_token, access_token_secret)
api = tw.API( auth )

tweets = api.search(q = input("Enter search term... "))
list_tweets = []
for tweet in tweets:
    list_tweets.append(tweet.text)

overall = 0
for tweet in list_tweets:
    blob = TextBlob(tweet)   
    print(tweet)
    avg = 0
    for sentence in blob.sentences:
        avg += sentence.sentiment.polarity
        avg /= len(blob.sentences)
    overall += avg
    print( avg, "Positive...." if avg>0.0 else( "Neutral..." if avg == 0.0 else "Negative...") )
overall /= len(list_tweets)
print( overall, "Overall..." if overall>0.0 else( "Neutral..." if overall == 0.0 else "Negative...") )  
