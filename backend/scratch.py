import pandas as pd

player_url = {}
for i in range(1,33):
    file_index = f'{i :03}'
    key = 'player_url_' + file_index
    player_url[key] = pd.read_csv('./dataset/url-images/image_file_' + file_index + '.csv')
    player_url[key] = player_url[key][['Player','PlayerURL']]

    
player_url_merged = pd.concat(player_url.values(), ignore_index=True)
print(player_url_merged)