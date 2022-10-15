import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:elonmusk) until:2021-01-01 since:2020-01-01"
tweets = []
limit = 50000
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    #print(vars(tweet))
    #break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date','User','Tweet'] )
print(df)

df.to_csv('tweet_extracted_trail.csv')


