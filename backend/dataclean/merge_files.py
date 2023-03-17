import pandas as pd

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