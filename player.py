#!/usr/bin/env python3
"""
CSC407 Network Analysis - Team Project
    @file player.py
Project Team Members:
    @author Michael McCulloch
    @author Ronald King
Due Date:
    @date 12/3/19
"""


# PlayerNode:
# A vertex object representing a player in the game
# name:  player/vertex number
# x_position:  x coordinate on xy axis
# y_position:  y coordinate on xy axis
# watching:  name of player/vertex looking at for time interval
# rumor:  boolean representing whether or not player has heard the rumor
class PlayerNode:

    # constructor
    def __init__(self, name):
        self.name = name
        self.x_position = 0
        self.y_position = 0
        self.watching = 0
        self.times_heard = 0
        self.rumor = False

    def is_watching(self):
        return self.watching

    def update_watching(self, name):
        self.watching = name

    def has_heard_rumor(self):
        return self.rumor

    def update_rumor(self, condition):
        self.rumor = condition

    def get_times_heard(self):
        return self.times_heard

    def increase_times_heard(self):
        self.times_heard += 1

