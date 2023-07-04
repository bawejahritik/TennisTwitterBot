# import tweepy
# import keys

# client = tweepy.Client(bearer_token=keys.bearer_token,
#                        consumer_key=keys.api_key,
#                        consumer_secret=keys.api_secret,
#                        access_token=keys.access_token,
#                        access_token_secret=keys.access_token_secret)

# auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
# api = tweepy.API(auth)

# client.create_tweet(text= "Hello World")
import requests
import keys

url = "https://sportscore1.p.rapidapi.com/sports/2/events/date/2023-07-03"

querystring = {"page":"1"}

headers = {
	"X-RapidAPI-Key": keys.new_key,
	"X-RapidAPI-Host": "sportscore1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

matches = response.json()["data"]

def remove(string):
    string = string.replace(" ", "")
    string = string.replace("&", "And")
    return string


# matches = {'id': 1910316, 'sport_id': 2, 'home_team_id': 13935, 'away_team_id': 12959, 'league_id': 7119, 'challenge_id': 44380, 'season_id': 31838, 'venue_id': 8229, 'referee_id': None, 'slug': '2023-07-03-baez-s-barrios-vera-t', 'name': 'Baez S. – Barrios Vera T.', 'status': 'finished', 'status_more': 'FT', 'time_details': {'currentPeriodStartTimestamp': 1688393593}, 'home_team': {'id': 13935, 'sport_id': 2, 'category_id': None, 'venue_id': None, 'manager_id': None, 'slug': 'baez-s', 'name': 'Baez S.', 'has_logo': True, 'logo': 'https://tipsscore.com/resb/team/baez-s.png', 
# 'name_translations': {'en': 'Baez S.', 'ru': 'Баэс, Себастьян', 'es': 'Baez, Sebastian', 'fr': 'Baez, Sebastian', 'zh': '贝斯，塞巴斯蒂安', 'pt': 'Sebastian Baez'}, 'name_short': 'Baez S.', 'name_full': 'Baez, Sebastian', 'name_code': 'BAE', 'has_sub': False, 'gender': 'M', 'is_nationality': False, 'country_code': 'ARG', 'country': 'Argentina', 'flag': 'argentina', 'foundation': None}, 'away_team': {'id': 12959, 'sport_id': 2, 'category_id': None, 'venue_id': None, 'manager_id': None, 'slug': 'barrios-vera-t', 'name': 'Barrios Vera T.', 'has_logo': True, 'logo': 'https://tipsscore.com/resb/team/barrios-vera-t.png', 'name_translations': {'en': 'Barrios Vera T.', 'ru': 'Барриос Вера, Марсело Томас', 'zh': ' 巴里奥斯·维拉，马塞洛·托马斯', 'el': 'Μπάριος Βέρα, Μαρσέλο Τόμας', 'pt': 'Tomas Barrios Vera', 'es': 'Barrios Vera, Marcelo Tomás'}, 'name_short': 'Barrios Vera T.', 'name_full': 'Barrios Vera, Tomás', 'name_code': 'BAR', 'has_sub': False, 'gender': 'M', 'is_nationality': False, 'country_code': 'CHL', 'country': 'Chile', 'flag': 'chile', 'foundation': None}, 'start_at': '2023-07-03 10:00:00', 'priority': 1, 'home_score': {'current': 1, 'display': 1, 'period_1': 6, 'period_2': 6, 'period_3': 3, 'period_4': 6, 'normal_time': 1, 'point': '2', 'period_1_tie_break': 7, 
# 'period_4_tie_break': 2}, 'away_score': {'current': 3, 'display': 3, 'period_1': 7, 'period_2': 3, 'period_3': 6, 'period_4': 7, 'normal_time': 3, 'point': '6', 'period_1_tie_break': 9, 'period_4_tie_break': 7}, 'winner_code': 2, 'aggregated_winner_code': None, 'result_only': False, 'coverage': None, 'ground_type': 'Grass', 'round_number': 64, 'series_count': 4, 'medias_count': None, 'status_lineup': None, 'first_supply': 1, 
# 'cards_code': None, 'event_data_change': None, 'lasted_period': 'period_4', 'default_period_count': 5, 'attendance': None, 'cup_match_order': None, 'cup_match_in_round': None, 'periods': {'current': 'Match', 'period_1': '1st set', 'period_2': '2nd set', 'period_3': '3rd set', 'period_4': '4th set', 'period_5': '5th set', 'point': 'Game'}, 'round_info': {'round': 64, 'name': 'Round of 128', 'slug': 'round-of-128'}, 'periods_time': {'period_1_time': 3978, 'period_2_time': 2657, 'period_3_time': 3017, 'period_4_time': 3348}, 'main_odds': {'outcome_1': {'value': 1.73, 'change': 1}, 'outcome_2': {'value': 2.1, 'change': -1}}, 'league': {'id': 7119, 'sport_id': 2, 'section_id': 145, 'slug': 'atp-wimbledon', 'name': 'Wimbledon', 'name_translations': {'en': 'Wimbledon'}, 'has_logo': True, 'logo': 'https://tipsscore.com/resb/league/atp-wimbledon.png'}, 'challenge': {'id': 44380, 'sport_id': 2, 'league_id': 7119, 'slug': 'wimbledon-28', 'name': 'Wimbledon', 'name_translations': {'en': 'Wimbledon'}, 'order': 0, 'priority': 0}, 'season': {'id': 31838, 'league_id': 7119, 'slug': '2023', 'name': 'Wimbledon Men Singles 2023', 'year_start': 2023, 'year_end': None}, 'section': {'id': 145, 'sport_id': 2, 'slug': 'atp', 'name': 'ATP', 'priority': 7, 'flag': 'atp'}, 'sport': {'id': 2, 'slug': 'tennis', 'name': 'Tennis'}}

# winner = ""
# loser = ""
# final_score = ""
# hashtags = ""

# tournament_name = matches["season"]["name"]
# round = matches["round_info"]["name"]

# if(matches["winner_code"] == 1):
#     winner = matches["home_team"]["name_translations"]["pt"]
#     loser =  matches["away_team"]["name_translations"]["pt"]
#     for key in matches["home_score"]:
#         if len(key) == 8:
#             final_score += (str(matches["home_score"][key])+"-"+str(matches["away_score"][key]) +", ")
# else:
#     winner = matches["away_team"]["name_translations"]["pt"]
#     loser = matches["home_team"]["name_translations"]["pt"]
#     for key in matches["away_score"]:
#         if len(key)==8:
#             final_score += (str(matches["away_score"][key])+"-"+str(matches["home_score"][key]))
#             if(matches["away_score"][key] == 7):
#                 final_score += ("("+str(matches["away_score"][key+"_tie_break"])+"-"+str(matches["home_score"][key+"_tie_break"])+")")
#             final_score += ", "
#     final_score = final_score[:len(final_score)-2]

# hashtags = "#" + remove(winner) + " #" + remove(loser) + " #" + remove(tournament_name) + "#" + remove(matches['challenge']['name']) + "#Tennis #ATP #WTA"
# print(tournament_name)
# print(round)
# print(winner + " vs " + loser)
# print(final_score)

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
        hashtags = "#" + remove(winner) + " #" + remove(loser) + " #" + remove(tournament_name) + " #" + remove(matches['challenge']['name']) + "#Tennis #ATP #WTA #TennisScoreFeed"
        print(tournament_name)
        print(round)
        print(winner + " vs " + loser)
        print(final_score)
        with open('temp.txt', 'w') as f:
            f.write(tournament_name + "\n\n" + winner + " def. " + loser + " "+ final_score + "\n\n\n\n" + hashtags)

        with open('temp.txt','r') as f:
            client.create_tweet(text=f.read())
                # print(f.read())

            # print(win + " defeats " + lost + " "+ final_score)
        numberOfTweets += 1
        if(numberOfTweets > 49):
            break