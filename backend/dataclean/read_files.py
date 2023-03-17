import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

def read():
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
    
    missing_players = player_names ^ player_names_merged
    missing_players = pd.DataFrame(missing_players, columns=['Players'])
    missing_players.to_csv('./cleaned-files/missing-players.csv')
    
    missing_players = pd.read_csv('./cleaned-files/missing-players.csv')

    player_url_merged = pd.concat([player_url_merged, missing_players]).drop('Unnamed: 0', axis=1).drop('Unnamed: 2', axis=1)

    player_url_merged = pd.merge(player_url_merged, missing_players, on="Player", how='left')
    player_url_merged.fillna("", inplace=True)
    player_url_merged = player_url_merged.concat()
    player_url_merged.to_csv('./cleaned-files/photoURL.csv')

    player_url_merged_1 = pd.DataFrame(columns=["Player","PlayerURL"])
    for index in range(1, 270):
        url = player_url_merged.iloc[index]['PlayerURL']
        name = player_url_merged.iloc[index]['Player']
        print(url, name)
        response = requests.get(url)
        time.sleep(2)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.find("img", alt=regex)
        try:
            image_url = links['src']
        except TypeError:
            image_url = ""
        player_url_merged_1.loc[index] = [name] + [image_url]
        print(f'Image URL complete for {index}/{len(player_url_merged)}')

    player_url_merged_1.to_csv('./cleaned-files/player-image-urls-1.csv')
    player_url_merged_1.head()

    # player_url_merged_1 = pd.DataFrame(columns=["Player","PlayerURL"])
    # player_url_merged_2 = pd.DataFrame(columns=["Player","PlayerURL"])
    # player_url_merged_3 = pd.DataFrame(columns=["Player","PlayerURL"])

    # player_url_merged_1.to_csv('./dataset/cleaned-files/player-image-urls-1.csv')
        
    # print(f'The len of the new set is {len(player_names ^ player_names_merged)} {player_names ^ player_names_merged}')
    # print(len(player_names), len(player_url_merged))

    return player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv