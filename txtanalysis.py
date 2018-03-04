from textblob import TextBlob
import tweepy as tw

consumer_key = 'mjdPNFSmi0VIfflurwkmgj8ff'
consumer_secret = 'ECpA6m5YVWfoxlnOuENOOOLTQKlP7E7kZ1QVMCH3Joo6X5pgPz'
access_token = '2741354322-pMH48FBZutbWGaYP4nO1sb8xWFbVCPfe23QUHeu'
access_token_secret = 'qcahLI7f1qVDbPboJOngHHasN7wCZaQ6bODkBtR8BHpLP'

auth = tw.OAuthHandler( consumer_key, consumer_secret)
auth.set_access_token( access_token, access_token_secret)
api = tw.API( auth )

tweets = api.search(q = input("Enter search term... "))
list_tweets = []
for tweet in tweets:
    list_tweets.append(tweet.text)

#text = '''Shrey is a bloody fool.'''
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
