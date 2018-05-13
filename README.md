# Stock Market Sentiment Analysis and Price Prediction 💹

### Importing modules

```python
# Matrix math and DataFrames
import numpy as np
import pandas as pd

# Scaling
from sklearn.preprocessing import MinMaxScaler
X_scaler = MinMaxScaler( feature_range = (-1,1))
y_scaler = MinMaxScaler( feature_range = (-1,1))

# Plotting
import plotly as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# Keras model and LSTM
from keras.models import Sequential
from keras.layers import LSTM,Dense
```

```python
# plotly offline config
py.offline.init_notebook_mode(connected=True)
```

## Retriving, Slicing and Dicing
Choosing the Facebook stock

### Use to fetch data from quandl
```python
import quandl as ql
ql.ApiConfig.api_key = "b6y7-mew_t8z5yGJijFv"
data = ql.get("WIKI/fb")
data.to_csv("Facebook", encoding='utf-8')
```

### Use the following code to generate Facebook_Sentiments.csv with sentiments
```python
from txtanalysis import *
tw = TweetSentiments()
sentiment_data =
pd.DataFrame(index=range( df.shape[0]),\
columns=['Sentiments'])
for i in range( train_limit):
    try :
sentiment_data['Sentiments'][i] = tw.get_input( '@facebook'\
, df['Date'][i])
    except tweepy.TweepError:
        time.sleep(60 * 15)
continue
    except StopIteration:
        break
df[:5]
sentiment_data.to_csv(
'Facebook_Sentiments', encoding='utf-8')
df.join( sentiment_data)
```

```python
df = pd.read_csv("Facebook")[['Date','Open','Close','High','Low']]
train_limit = round(df.shape[0]*0.8)
print(train_limit)
df[:5]
```

# Data transformation

## Scaling
Warning! DataFrames will be changed after this...

```python
df = pd.read_csv('Facebook_Sentiments')
df = df[['Open','Close','High','Low','Sentiments']]
df[['Open','High','Low','Sentiments']] = X_scaler.fit_transform(df[['Open','High','Low','Sentiments']])
df[['Close']] = y_scaler.fit_transform(df[['Close']])
```

## Splitting into train, validate and test sets

```python
sequence_len = 20 # choose sequence length

train_data = pd.DataFrame( columns = ['Open','Close','High','Low','Sentiments'])
valid_limit = train_limit + round(df.shape[0]*0.1)
test_limit = -1*round(df.shape[0]*0.1)

# create all possible sequences of length sequence_len
validate_data = df[train_limit: valid_limit]
test_data = df[ test_limit :-1 ]

df = df[:train_limit]

for index in range( train_limit - sequence_len):
    train_data = train_data.append( df[index: index + sequence_len])

print( train_data[:5], validate_data[-5:-1] ,test_data[:5])

X_train = train_data[['Open','High','Low','Sentiments']].as_matrix().reshape( train_data.shape[0], 1, 4)
y_train = train_data[['Close']].as_matrix().flatten()

X_valid = validate_data[['Open','High','Low','Sentiments']].as_matrix().reshape( validate_data.shape[0], 1, 4)
y_valid = validate_data[['Close']].as_matrix().flatten()

X_test = test_data[['Open','High','Low','Sentiments']].as_matrix().reshape( test_data.shape[0], 1, 4)
y_test = test_data[['Close']].as_matrix().flatten()
print(X_train.shape, y_train.shape)
```

## Building and training the LSTM

```python
#Build the model
model = Sequential()
model.add(LSTM(256,input_shape=( 1, 4)))
model.add(Dense(1))
model.compile(optimizer='adam',loss='mse')
#Fit model with history to check for overfitting
history = model.fit( X_train, y_train, epochs=20, validation_data=(X_valid,y_valid), shuffle=True)
```
* Red -> Test Data
* Green -> Predicted Data
![Alt](/Screenshots/valid.png "Test vs Predicted plot")

> Training observations
* Overfitting occurs at approx. 20 epochs
* 1e-5 to 9e-5
validation loss with shuffle
* 0.0322 to 6e-4 validation loss without shuffle

> Licenced under MIT &copy; Yash Tripathi
