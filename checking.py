import requests
from datetime import datetime, timezone
import tweepy
import os
import keys

def remove(string):
    string = string.replace(" ", "")
    string = string.replace("&", "And")
    return string

# client = tweepy.Client(bearer_token=os.environ["bearer_token"],
#                        consumer_key=os.environ["api_key"],
#                        consumer_secret=os.environ["api_key_secret"],
#                        access_token=os.environ["access_token"],
#                        access_token_secret=os.environ["access_token_secret"])

# client = tweepy.Client(bearer_token=keys.bearer_token,
#                        consumer_key=keys.api_key,
#                        consumer_secret=keys.api_secret,
#                        access_token=keys.access_token,
#                        access_token_secret=keys.access_token_secret)

# auth = tweepy.OAuthHandler(os.environ["api_key"], 
#                            os.environ["api_key_secret"], 
#                            os.environ["access_token"], 
#                            os.environ["access_token_secret"])

# auth = tweepy.OAuthHandler(keys.api_key, 
#                            keys.api_secret, 
#                            keys.access_token, 
#                            keys.access_token_secret)
# api = tweepy.API(auth)

currentDate = datetime.now(timezone.utc).strftime("%Y-%m-%d")

url = "https://sportscore1.p.rapidapi.com/sports/2/events/date/2023-07-03"

querystring = {"page":"1"}

headers = {
	"X-RapidAPI-Key": keys.new_key,
	"X-RapidAPI-Host": "sportscore1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

matches = response.json()["data"]

numberOfTweets = 0

for match in matches:
    if match["status"] == "finished" and (match["section"]["name"] == "ATP" or match["section"]["name"] == "WTA"):
        winner = ""
        loser = ""
        final_score = ""

        tournament_name = match["season"]["name"]
        round = match["round_info"]["name"]

        if(match["winner_code"] == 1):
            winner = match["home_team"]["name_translations"]["pt"]
            loser =  match["away_team"]["name_translations"]["pt"]
            for key in match["home_score"]:
                if len(key) == 8:
                    final_score += (str(match["home_score"][key])+"-"+str(match["away_score"][key]))
                    if(match["home_score"][key] == 7 and match["away_score"][key] == 6):
                        final_score += ("("+str(match["home_score"][key+"_tie_break"])+"-"+str(match["away_score"][key+"_tie_break"])+")")
                    final_score += ", "
        else:
            winner = match["away_team"]["name_translations"]["pt"]
            loser = match["home_team"]["name_translations"]["pt"]
            for key in match["away_score"]:
                if len(key)==8:
                    final_score += (str(match["away_score"][key])+"-"+str(match["home_score"][key]))
                    if(match["away_score"][key] == 7 and match["home_score"][key] == 6):
                        final_score += ("("+str(match["away_score"][key+"_tie_break"])+"-"+str(match["home_score"][key+"_tie_break"])+")")
                    final_score += ", "
            
        final_score = final_score[:len(final_score)-2]
        hashtags = "#" + remove(winner) + " #" + remove(loser) + " #" + remove(tournament_name) + " #" + remove(match["challenge"]["name"]) + " #Tennis #ATP #WTA #TennisScoreFeed"
        numberOfTweets += 1
        print(numberOfTweets)
        print(tournament_name)
        print(round)
        print(winner + " vs " + loser)
        print(final_score + "\n\n")
        # with open('temp.txt', 'w') as f:
        #     f.write(tournament_name + "\n\n" +round + "\n"+ winner + " def. " + loser + " "+ final_score + "\n\n\n\n" + hashtags)

        # with open('temp.txt','r') as f:
        #     client.create_tweet(text=f.read())
                #print(f.read())

            # print(win + " defeats " + lost + " "+ final_score)
        
        # if(numberOfTweets > 49):
        #     break