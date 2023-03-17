import pandas as pd

def split(allPlayers, player_keepers, player_keepersadv):
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