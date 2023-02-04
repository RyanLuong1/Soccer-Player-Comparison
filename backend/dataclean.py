import pandas as pd
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from io import StringIO
import requests
import re
from lxml import html
from ip import get_proxies
from itertools import cycle

def read_files():
    # Reads csv files via pandas and returns them

    # Stats
    player_defense = pd.read_csv('./dataset/player_defense.csv')
    player_gca = pd.read_csv('./dataset/player_gca.csv')
    player_misc = pd.read_csv('./dataset/player_misc.csv')
    player_passing_types = pd.read_csv('./dataset/player_passing_types.csv')
    player_possession = pd.read_csv('./dataset/player_possession.csv')
    player_shooting = pd.read_csv('./dataset/player_shooting.csv')
    player_stats = pd.read_csv('./dataset/player_stats.csv')
    player_passing = pd.read_csv('./dataset/player_passing.csv')
    player_keepers = pd.read_csv('./dataset/player_keepers.csv')
    player_keepersadv = pd.read_csv('./dataset/player_keepersadv.csv')
    player_names = player_defense[['player']]

    # Player Profile URL
    player_url = {}
    for i in range(1,33):
        file_index = f'{i :03}'
        key = 'player_url_' + file_index
        player_url[key] = pd.read_csv('./dataset/url-images/image_file_' + file_index + '.csv')
        player_url[key] = player_url[key][['Player','PlayerURL']]

    player_url_merged = pd.concat(player_url.values(), ignore_index=True)    

    player_names = set([names for names in player_names['player']])

    for idx in range(len(player_url_merged[['Player']])):
        if player_url_merged.iloc[idx]['Player'] not in player_names:
            player_url_merged.iloc[idx]['Player'] = None
            player_url_merged.iloc[idx]['PlayerURL'] = None
    
    player_url_merged.dropna(inplace=True)
    
    player_names_merged = set([names for names in player_url_merged['Player']])
    
    # missing_players = player_names ^ player_names_merged
    # missing_players = pd.DataFrame(missing_players, columns=['Players'])
    # missing_players.to_csv('./cleaned-files/missing-players.csv')
    
    missing_players = pd.read_csv('./cleaned-files/missing-players.csv')

    player_url_merged = pd.concat([player_url_merged, missing_players]).drop('Unnamed: 0', axis=1).drop('Unnamed: 2', axis=1)

    # player_url_merged = pd.merge(player_url_merged, missing_players, on="Player", how='left')
    # player_url_merged.fillna("", inplace=True)
    # player_url_merged = player_url_merged.concat()
    player_url_merged.to_csv('./cleaned-files/photoURL.csv')
    ip_list = list(get_proxies())
    ip_cycle = cycle(ip_list)

    regex = re.compile('.*headshot*.')
    for idx in range(len(player_url_merged[['Player']])):
        url = player_url_merged.iloc[idx]['PlayerURL']
        proxy = next(ip_cycle)
    
        response = requests.get(url, proxies={"http": f'http://{proxy}', "https": f'http://{proxy}'})
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find("img", alt=regex)
        player_url_merged.iloc[idx]['PlayerURL'] = links['src']
        print(player_url_merged.iloc[idx])
        if idx == 2:
            exit()
        
    # print(f'The len of the new set is {len(player_names ^ player_names_merged)} {player_names ^ player_names_merged}')
    # print(len(player_names), len(player_url_merged))

    


    return player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv


def merge(player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv):
    # manipulates csv data to use only useful columns, coverts into dataframes, merges into one, and returns main dataframes
    
    player_gca=pd.DataFrame(player_gca.drop(player_gca.iloc[:, 0:6], axis=1))
    player_misc=pd.DataFrame(player_misc.drop(player_misc.iloc[:, 0:6], axis=1))
    player_passing_types=pd.DataFrame(player_passing_types.drop(player_passing_types.iloc[:, 0:6], axis=1))
    player_passing=pd.DataFrame(player_passing.drop(player_passing.iloc[:, 0:6], axis=1))
    player_possession=pd.DataFrame(player_possession.drop(player_possession.iloc[:, 0:6], axis=1))
    player_shooting=pd.DataFrame(player_shooting.drop(player_shooting.iloc[:, 0:6], axis=1))
    player_stats=pd.DataFrame(player_stats.drop(player_stats.iloc[:, 0:6], axis=1))

    allPlayers = pd.concat([player_defense, player_gca, player_misc, player_passing_types, 
                        player_passing, player_possession, 
                        player_shooting, player_stats], axis=1)

    # remove duplicate columns
    allPlayers = allPlayers.loc[:,~allPlayers.columns.duplicated()].copy()
    allPlayers.to_csv('./cleaned-files/AllPlayers.csv')

    return allPlayers


def split(allPlayers):
    position = {
        "GK": "Goalkeeper",
        "DF": "Defender",
        "FB": "Defender",
        "LB": "Defender",
        "RB": "Defender",
        "CB": "Defender",
        "MF": "Midfielder", 
        "DM": "Midfielder", 
        "CM": "Midfielder", 
        "LM": "Midfielder", 
        "RM": "Midfielder", 
        "WM": "Midfielder",
        "LW": "Forward",
        "RW": "Forward",
        "AM": "Forward",
        "FW": "Forward"
    }
    
    goalkeepers = pd.DataFrame(columns = allPlayers.columns)
    defenders = pd.DataFrame(columns = allPlayers.columns)
    midfielders = pd.DataFrame(columns = allPlayers.columns)
    forwards = pd.DataFrame(columns = allPlayers.columns)
    
    for idx in range(len(allPlayers)):
        play_pos_abrv = allPlayers['position'][idx]
        play_pos = position[play_pos_abrv]
        player_to_add = allPlayers.loc[idx]
        if play_pos == "Defender":
            defenders.loc[len(defenders)] = player_to_add
        elif play_pos == "Midfielder":
            midfielders.loc[len(midfielders)] = player_to_add
        elif play_pos == "Forward":
            forwards.loc[len(forwards)] = player_to_add
        else:
            goalkeepers.loc[len(goalkeepers)] = player_to_add

    goalkeepers = goalkeepers[['tackles_interceptions', 'clearances', 'errors', 'ball_recoveries', 
            'aerials_won', 'aerials_lost', 'passes', 'passes_live', 'passes_dead', 'passes_free_kicks', 
            'passes_completed', 'passes_pct', 'passes_total_distance', 'passes_progressive_distance', 
            'passes_pct_short', 'passes_pct_medium', 'passes_pct_long', 'passes_into_final_third', 'touches']]

    goalkeepers = pd.concat([player_keepers, player_keepersadv, goalkeepers], axis=1)
    goalkeepers = goalkeepers.loc[:,~goalkeepers.columns.duplicated()].copy()

    goalkeepers.to_csv('./cleaned-files/goalkeeper.csv')
    defenders.to_csv('./cleaned-files/defenders.csv')
    midfielders.to_csv('./cleaned-files/midfielders.csv')
    forwards.to_csv('./cleaned-files/forwards.csv')

if __name__ == '__main__':

    player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv = read_files()
    allPlayers = merge(player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv)
    split(allPlayers)