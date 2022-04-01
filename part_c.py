#!/usr/bin/env python3
"""
CSC407 Network Analysis - Team Project
    @file part_c.py
Project Team Members:
    @author Michael McCulloch
    @author Ronald King
Due Date:
    @date 12/3/19
"""


# Add imports, variable definitions, and constants here
import random
import player
import utilities


# Part_C:
# Probability of rumor spreading through face-to-face interactions
# where each graph connection at interval has probability p of spreading rumor
# input parameter p_value: probability of rumor spreading
# input parameter start: initial player that starts rumor
# input parameter n: number of iterations to be run
# input parameter output_file: external output file
def part_c(p_value, start, n, output_file):

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

    # Open network5.csv file
    with open('./network/network5.csv', 'r') as f:
        # Skip first 6500 time segments (slightly more than 2/3 way through the game)
        for _ in range(6501):
            next(f)
        for line in f:
            line_data = (line.split(","))

            # Outer loop for i players
            counter = 0
            for i in range(1, count + 1):
                # Inner loop for who player is looking at
                for j in range(count + 1):
                    counter += 1
                    if int(line_data[counter]) == 1:
                        # Set player looking at
                        ply[i].update_watching(j)
                        if j == 0:
                            continue
                        elif ply[i].has_heard_rumor() and not ply[j].has_heard_rumor():
                            r = random.random()
                            if p_value > r:
                                ply[j].update_rumor(True)
                                path.append([i, j])

    # Output rumor status to file
    utilities.output_record(output_file, n, ply)
    print(path)


def main():

    # Set p-value
    p = 0.0025

    # Set initial player to start rumor
    start = 3

    # Set number of iterations to be run
    run_count = 50

    # Create and open output file for storing rumor spread status
    with open('part_c_output.csv', 'w') as output_file:
        # write headers to output file
        output_file.write('RUN NO.,' + 'LAP,' + 'P1,' + 'P2,' + 'P3,' + 'P4,' + 'P5,' + 'P6,' + 'P7,' + 'P8' + '\n')

        # Run multiple iterations with p-value
        for n in range(run_count):
            part_c(p, start, n, output_file)


main()
