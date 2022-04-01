"""
CSC407 Network Analysis - Team Project
    @file utilities.py
Project Team Members:
    @author Michael McCulloch
    @author Ronald King
Due Date:
    @date 12/3/19
"""


# Add imports, variable definitions, and constants here
import linecache


# Variable Definitions, Functions, and Constants

# Minimum and Maximum allowable number of players for a Resistance game
MIN_PLAYERS_ALLOWED = 5
MAX_PLAYERS_ALLOWED = 10

# X and Y positional values (coordinates) for location of player nodes
# note: only required if template not used
X_POSITION = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Y_POSITION = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Utility function to retrieve number of players in game from from network_list.csv file
# input parameter game: integer corresponding to game number to retrieve player count
# output parameter count: integer corresponding to number of players in the game
def get_player_count(game):
    line_data = linecache.getline("network_list.csv", game + 1)
    line_data = (line_data.split(","))
    count = int(line_data[1])
    if count < MIN_PLAYERS_ALLOWED or count > MAX_PLAYERS_ALLOWED:
        return -1
    return count


# Utility function to output rumor status to external file
# input parameter output_file:  external file
# input parameter n:  game number
# input parameter plyr: list of player nodes
def output_record(output_file, n, plyr):

    # Add game number
    output_file.write(str(n + 1) + ',')

    # Add rumor status for each player
    for pl in plyr:
        separator = ","
        output_file.write(str(pl.has_heard_rumor()) + separator)
    output_file.write('\n')