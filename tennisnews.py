import feedparser
import tweepy
import os

client = tweepy.Client(bearer_token=os.environ["bearer_token"],
                       consumer_key=os.environ["api_key"],
                       consumer_secret=os.environ["api_key_secret"],
                       access_token=os.environ["access_token"],
                       access_token_secret=os.environ["access_token_secret"],
                       wait_on_rate_limit=True)

# client = tweepy.Client(bearer_token=bearer_token,
#                        consumer_key=consumer_key,
#                        consumer_secret=consumer_secret,
#                        access_token=access_token,
#                        access_token_secret=access_token_secret)

auth = tweepy.OAuthHandler(os.environ["api_key"], 
                           os.environ["api_key_secret"], 
                           os.environ["access_token"], 
                           os.environ["access_token_secret"])


# Authenticate to Twitter
api = tweepy.API(auth)

# RSS Feed URL for climate technology news
rss_url = 'https://www.atptour.com/en/media/rss-feed/xml-feed'

# Fetching and posting the latest news
def post_latest_news():
    feed = feedparser.parse(rss_url)
    latest_entry = feed

    print(latest_entry.keys())

    print(len(latest_entry.entries))

    
    for entry in latest_entry.entries:
        file_data = ""
        print(entry.keys())
        print(entry.link)
        print(entry.title)
        print(entry.tags)
        print("--------------------------------------------------------")
        file_data += entry.title
        file_data += '\n'
        file_data += entry.link
        file_data += '\n'
        file_data += "#Tennis #ATP #WTA #TennisScoreFeed"

        with open('temp1.txt', 'w', encoding='utf-8') as f:
            f.write(file_data)

        try:
            with open('temp1.txt','r', encoding='utf-8') as f:
                client.create_tweet(text=f.read())
        except:
            pass


    
if __name__ == "__main__":
    post_latest_news()
