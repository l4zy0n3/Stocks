from tweetanalysis import *
import pandas as pd

df = pd.read_csv('Facebook')[['Date', 'Open', 'Close', 'High', 'Low']]
df['Sentiments'] = 0.0
df['Sentiments'] = df['Date'].apply( lambda x: TweetSentiments( 'facebook', x).calculate())
df.to_csv( 'Facebook_Sentiments', encoding = 'utf-8')