import pandas as pd
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from io import StringIO
import requests
import re

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

    # Player URL Player, PlayerURL
    player_url_001 = pd.read_csv('./dataset/url-images/image_file_001.csv')
    player_url_002 = pd.read_csv('./dataset/url-images/image_file_002.csv')
    player_url_003 = pd.read_csv('./dataset/url-images/image_file_003.csv')
    player_url_004 = pd.read_csv('./dataset/url-images/image_file_004.csv')
    player_url_005 = pd.read_csv('./dataset/url-images/image_file_005.csv')
    player_url_006 = pd.read_csv('./dataset/url-images/image_file_006.csv')
    player_url_007 = pd.read_csv('./dataset/url-images/image_file_007.csv')
    player_url_008 = pd.read_csv('./dataset/url-images/image_file_008.csv')
    player_url_009 = pd.read_csv('./dataset/url-images/image_file_009.csv')
    player_url_010 = pd.read_csv('./dataset/url-images/image_file_010.csv')
    player_url_011 = pd.read_csv('./dataset/url-images/image_file_011.csv')
    player_url_012 = pd.read_csv('./dataset/url-images/image_file_012.csv')
    player_url_013 = pd.read_csv('./dataset/url-images/image_file_013.csv')
    player_url_014 = pd.read_csv('./dataset/url-images/image_file_014.csv')
    player_url_015 = pd.read_csv('./dataset/url-images/image_file_015.csv')
    player_url_016 = pd.read_csv('./dataset/url-images/image_file_016.csv')
    player_url_017 = pd.read_csv('./dataset/url-images/image_file_017.csv')
    player_url_018 = pd.read_csv('./dataset/url-images/image_file_018.csv')
    player_url_019 = pd.read_csv('./dataset/url-images/image_file_019.csv')
    player_url_020 = pd.read_csv('./dataset/url-images/image_file_020.csv')
    player_url_021 = pd.read_csv('./dataset/url-images/image_file_021.csv')
    player_url_022 = pd.read_csv('./dataset/url-images/image_file_022.csv')
    player_url_023 = pd.read_csv('./dataset/url-images/image_file_023.csv')
    player_url_024 = pd.read_csv('./dataset/url-images/image_file_024.csv')
    player_url_025 = pd.read_csv('./dataset/url-images/image_file_025.csv')
    player_url_026 = pd.read_csv('./dataset/url-images/image_file_026.csv')
    player_url_027 = pd.read_csv('./dataset/url-images/image_file_027.csv')
    player_url_028 = pd.read_csv('./dataset/url-images/image_file_028.csv')
    player_url_029 = pd.read_csv('./dataset/url-images/image_file_029.csv')
    player_url_030 = pd.read_csv('./dataset/url-images/image_file_030.csv')
    player_url_031 = pd.read_csv('./dataset/url-images/image_file_031.csv')
    player_url_032 = pd.read_csv('./dataset/url-images/image_file_032.csv')

    #Get all the names from line 7 - 17 and put it in a set
    #read one file (player_defnse) get it through column, get all the names to a set
    #Iterate player_url csv, check the column ('Player')
    #Go through all the player url rows and check if their name is in the set
    #If it does not exist in the set, erase the whole row
    #If it does, do nothing

    player_url_001 = player_url_001[['Player', 'PlayerURL']]
    player_url_002 = player_url_002[['Player', 'PlayerURL']]
    player_url_003 = player_url_003[['Player', 'PlayerURL']]
    player_url_004 = player_url_004[['Player', 'PlayerURL']]
    player_url_005 = player_url_005[['Player', 'PlayerURL']]
    player_url_006 = player_url_006[['Player', 'PlayerURL']]
    player_url_007 = player_url_007[['Player', 'PlayerURL']]
    player_url_008 = player_url_008[['Player', 'PlayerURL']]
    player_url_009 = player_url_009[['Player', 'PlayerURL']]
    player_url_010 = player_url_010[['Player', 'PlayerURL']]
    player_url_011 = player_url_011[['Player', 'PlayerURL']]
    player_url_012 = player_url_012[['Player', 'PlayerURL']]
    player_url_013 = player_url_013[['Player', 'PlayerURL']]
    player_url_014 = player_url_014[['Player', 'PlayerURL']]
    player_url_015 = player_url_015[['Player', 'PlayerURL']]
    player_url_016 = player_url_016[['Player', 'PlayerURL']]
    player_url_017 = player_url_017[['Player', 'PlayerURL']]
    player_url_018 = player_url_018[['Player', 'PlayerURL']]
    player_url_019 = player_url_019[['Player', 'PlayerURL']]
    player_url_020 = player_url_020[['Player', 'PlayerURL']]
    player_url_021 = player_url_021[['Player', 'PlayerURL']]
    player_url_022 = player_url_022[['Player', 'PlayerURL']]
    player_url_023 = player_url_023[['Player', 'PlayerURL']]
    player_url_024 = player_url_024[['Player', 'PlayerURL']]
    player_url_025 = player_url_025[['Player', 'PlayerURL']]
    player_url_026 = player_url_026[['Player', 'PlayerURL']]
    player_url_027 = player_url_027[['Player', 'PlayerURL']]
    player_url_028 = player_url_028[['Player', 'PlayerURL']]
    player_url_029 = player_url_029[['Player', 'PlayerURL']]
    player_url_030 = player_url_030[['Player', 'PlayerURL']]
    player_url_031 = player_url_031[['Player', 'PlayerURL']]
    player_url_032 = player_url_032[['Player', 'PlayerURL']]

    player_url_merged = pd.concat([player_url_001, player_url_002, player_url_003, 
                                    player_url_004, player_url_005, player_url_006, 
                                    player_url_007, player_url_008, player_url_009, 
                                    player_url_010, player_url_011, player_url_012, 
                                    player_url_013, player_url_014, player_url_015, 
                                    player_url_016, player_url_017, player_url_018, 
                                    player_url_019, player_url_020, player_url_021, 
                                    player_url_022, player_url_023, player_url_024, 
                                    player_url_025,  player_url_026,  
                                    player_url_027, player_url_028, player_url_029, 
                                    player_url_030, player_url_031, player_url_032])
    
    #Get all the names from line 7 - 17 and put it in a set
    #read one file (player_defnse) get it through column, get all the names to a set
    #Iterate player_url csv, check the column ('Player')
    #Go through all the player url rows and check if their name is in the set
    #If it does not exist, do nothing
    #If it does, move it to something else

    # player_url_merged = 1300
    # most of them dont exist in our stats db
    # removing the ones that do not exist in stats db
    # line 126, we dropped the names
    # line 130, we got the missing names; we trying to do: missing names + player_url_merged = stats db
    # we want to merge based on player 
    # line 134, add rows to player_url_merged from missing_players
    # player_url_merged[player] += missing_player[player]
    

    player_names = set([names for names in player_names['player']])

    for idx in range(len(player_url_merged[['Player']])):
        if player_url_merged.iloc[idx]['Player'] not in player_names:
            player_url_merged.iloc[idx]['Player'] = None
            player_url_merged.iloc[idx]['PlayerURL'] = None
    # player_url_merged = player_url_merged[player_url_merged['Player'] == ""]
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
    
    regex = re.compile('.*headshot*.')
    for idx in range(len(player_url_merged[['Player']])):
        url = player_url_merged.iloc[idx]['PlayerURL']
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find('img', alt= regex)
        # links = soup.find_all('img', {"alt": 'headshot'})
        player_url_merged.iloc[idx]['PlayerURL'] = links['src']
        print(player_url_merged.iloc[idx])
        
    # print(f'The len of the new set is {len(player_names ^ player_names_merged)} {player_names ^ player_names_merged}')
    # print(len(player_names), len(player_url_merged))
    exit()
    


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