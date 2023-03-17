import pandas as pd
from io import StringIO
import re
from lxml import html
from ip import get_proxies
from itertools import cycle 

import read_files, merge_files, split_files

if __name__ == '__main__':

    player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv = read_files.read()
    allPlayers = merge_files.merge(player_defense, player_gca, player_misc, player_passing_types, player_possession, player_shooting, player_stats, player_passing, player_keepers, player_keepersadv)
    split_files.split(allPlayers, player_keepers, player_keepersadv)