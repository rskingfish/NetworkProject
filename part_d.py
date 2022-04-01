#!/usr/bin/env python3
"""
CSC407 Network Analysis - Team Project
    @file part_d.py
Project Team Members:
    @author Michael McCulloch
    @author Ronald King
Due Date:
    @date 12/3/19
"""


# Add imports, variable definitions, and constants here
import random
import utilities
import player


# Part_D:
# Probability of rumor spreading through face-to-face interactions
# where each graph connection at interval has probability weighted p of spreading rumor
# input parameter start: initial player that starts rumor
# input parameter n: number of iterations to be run
# input parameter output_file: external output file
def part_d(p_value, start, n, redux, output_file):

    # Retrieve number of players in game
    count = utilities.get_player_count(5)
    if count == -1:
        print("Number of players is outside of game parameters.")
        exit(1)

    # Create the players (note: ply[0] = laptop)
    ply = []
    for i in range(count + 1):
        ply.append(player.PlayerNode(i))

    # Establish a player as having heard the rumor (person who starts rumor)
    ply[start].update_rumor(True)

    # Path of rumor spread
    path = [start]

    # Open network5_weighted.csv file and read in data
    with open('./network/network5_weighted.csv', 'r') as f:
        # Skip first 6500 time segments (slightly more than 2/3 way through the game)
        for _ in range(6501):
            next(f)
        for line in f:
            line_data = (line.split(","))

            r = random.random()

            # Loop for i players
            for i in range(1, count + 1):
                # create sublist for each player
                sublist = line_data[(count + 1) * (i - 1) + 1:(count + 1) * i + 1]
                sum_list = 0
                for sub in range(len(sublist)):
                    sum_list += float(sublist[sub])
                for sub in range(len(sublist)):
                    if sub == 0:
                        continue
                    elif ply[i].has_heard_rumor() and not ply[sub].has_heard_rumor():
                        if (float(sublist[sub]) * p_value)/(sum_list * redux) > r:
                            ply[sub].increase_times_heard()
                            if ply[sub].get_times_heard() == 1:
                                ply[sub].update_rumor(True)
                                path.append((i, sub))

    # Output rumor status to file
    utilities.output_record(output_file, n, ply)
    print(path)


def main():

    # Set p-value
    p = 0.001

    # Set initial player to start rumor
    start = 1

    # Set number of iterations to be run
    run_count = 25

    # Set p reduction divisor
    redux = 1

    # Create and open output file for storing rumor spread status
    with open('part_d_output.csv', 'w') as output_file:
        # write headers to output file
        output_file.write('RUN NO.,' + 'LAP,' + 'P1,' + 'P2,' + 'P3,' + 'P4,' + 'P5,' + 'P6,' + 'P7,' + 'P8' + '\n')

        # Run multiple iterations
        for n in range(run_count):
            part_d(p, start, n, redux, output_file)


main()
