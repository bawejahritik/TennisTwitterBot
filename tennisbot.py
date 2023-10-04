import tweepy
import keys

import time

import requests
from datetime import datetime, timezone
import os



def remove(string):
    if(len(string)==0):
        return string
    string = string.replace(" ", "")
    string = string.replace("&", "And")
    string = string.replace("-", "")
    string = string.replace(",", "")
    string = string.replace("'", "")
    return string

# client = tweepy.Client(bearer_token=os.environ["bearer_token"],
#                        consumer_key=os.environ["api_key"],
#                        consumer_secret=os.environ["api_key_secret"],
#                        access_token=os.environ["access_token"],
#                        access_token_secret=os.environ["access_token_secret"],
#                        wait_on_rate_limit=True)

client = tweepy.Client(bearer_token=keys.bearer_token,
                       consumer_key=keys.api_key,
                       consumer_secret=keys.api_secret,
                       access_token=keys.access_token,
                       access_token_secret=keys.access_token_secret)

# auth = tweepy.OAuthHandler(os.environ["api_key"], 
#                            os.environ["api_key_secret"], 
#                            os.environ["access_token"], 
#                            os.environ["access_token_secret"])

auth = tweepy.OAuthHandler(keys.api_key, 
                           keys.api_secret, 
                           keys.access_token, 
                           keys.access_token_secret)

api = tweepy.API(auth)

currentDate = datetime.now(timezone.utc).strftime("%Y-%m-%d")

url = "https://sportscore1.p.rapidapi.com/sports/2/events/date/" + currentDate
# url = "https://sportscore1.p.rapidapi.com/sports/2/events/date/2023-07-16"

querystring = {"page":"1"}

headers = {
	"X-RapidAPI-Key": os.environ["rapid_api_key"],
    # "X-RapidAPI-Key": keys.rapid_api_key,
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
        flag = False
        
        tournament_name = match["season"]["name"]
        qualify = match["challenge"]["name"]
        
        if("Double" in tournament_name or "Qualifying" in qualify):
            flag = True
        elif(match["winner_code"] == 1):
            # print(match)
            round = match["round_info"]["name"]
            try:
                winner = match["home_team"]["name_translations"]["pt"]
            except:
                winner = match["home_team"]["name_full"]
                if(winner == None):
                    winner = match["home_team"]["name"]
            try:
                loser =  match["away_team"]["name_translations"]["pt"]
            except:
                loser = match["away_team"]['name_full']
                if( loser == None):
                    loser = match["away_team"]["name"]
                
            for key in match["home_score"]:
                if len(key) == 8:
                    final_score += (str(match["home_score"][key])+"-"+str(match["away_score"][key]))
                    if(match["home_score"][key] == 7 and match["away_score"][key] == 6):
                        final_score += ("("+str(match["home_score"][key+"_tie_break"])+"-"+str(match["away_score"][key+"_tie_break"])+")")
                    elif(match["away_score"][key] == 7 and match["home_score"][key] == 6):
                        final_score += ("("+str(match["away_score"][key+"_tie_break"])+"-"+str(match["home_score"][key+"_tie_break"])+")")
                    final_score += ", "
        else:
            # print(match)
            round = match["round_info"]["name"]
            try:
                winner = match["away_team"]["name_translations"]["pt"]
            except:
                winner = match["away_team"]["name_full"]
                if(winner == None):
                    winner = match["away_team"]["name"]
            try:
                loser = match["home_team"]["name_translations"]["pt"]
            except:
                loser = match["home_team"]["name_full"]
                if(loser == None):
                    loser = match["home_team"]["name"]

            for key in match["away_score"]:
                if len(key)==8:
                    final_score += (str(match["away_score"][key])+"-"+str(match["home_score"][key]))
                    if(match["away_score"][key] == 7 and match["home_score"][key] == 6):
                        final_score += ("("+str(match["away_score"][key+"_tie_break"])+"-"+str(match["home_score"][key+"_tie_break"])+")")
                    elif(match["home_score"][key] == 7 and match["away_score"][key] == 6):
                        final_score += ("("+str(match["home_score"][key+"_tie_break"])+"-"+str(match["away_score"][key+"_tie_break"])+")")
                    final_score += ", "
        if(flag != True):
            final_score = final_score[:len(final_score)-2]
            # print(tournament_name)
            # print(round)
            # print(winner + " vs " + loser)
            # print(match["challenge"]["name"])
            # print(final_score + "\n\n")
            media_ids = []

            if(match["home_team"]["has_logo"]):
                url = match["home_team"]["logo"]
                response = requests.get(url)
                with open("home_team.jpg", "wb") as f:
                    f.write(response.content)
                media_ids.append(api.media_upload("home_team.jpg").media_id)
                    
            if(match["away_team"]["has_logo"]):
                url = match["away_team"]["logo"]
                response = requests.get(url)
                with open("away_team.jpg", "wb") as f:
                    f.write(response.content)
                media_ids.append(api.media_upload("away_team.jpg").media_id)
                

            hashtags = "#" + remove(winner) + " #" + remove(loser) + " #" + remove(tournament_name) + " #" + remove(match["challenge"]["name"]) + " #Tennis #ATP #WTA #TennisScoreFeed #TennisFans #TennisPlayers #TennisCommunity #TennisMatchday"

            with open('temp.txt', 'w') as f:
                f.write("🎾 " + tournament_name + " - " + round + " 🏆\n\n"+ winner + " def. " + loser + " "+ final_score + "\n\nStay tuned for more exciting tennis updates! 📊\n\n" + hashtags)

            with open('temp.txt','r') as f:
                time.sleep(1)
                client.create_tweet(text=f.read(), media_ids=media_ids)
                # print(f.read())
            numberOfTweets += 1
            # print(numberOfTweets)
            # print(winner + " defeats " + loser + " "+ final_score)
            # numberOfTweets += 1
            # if(numberOfTweets > 49):
            #     break