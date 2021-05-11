# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

'''
Assignment 'strings' for WincAcademy Data Analysis course

version 1.0
Created by Wim Brouwer
Date of creation 11/05/2021
'''

#PART 1

# Scoring player list
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'

player_list = [player_1, player_2]

# Goal timing list
goal_1 = 32 #minutes
goal_2 = 54 #minutes

goal_list = [goal_1, goal_2]

# Reporter comments <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = player_list[0] + ' ' + str(goal_list[0]) + ', ' + player_list[1] + ' ' + str(goal_list[1])

report = str(f'{player_list[0]} scored in the {str(goal_list[0])}nd minute \n{player_list[1]} scored in the {str(goal_list[1])}th minute')

print(report)

#PART 2

player = "John van 't Schip"

first_name = player[:player.find(' ')]               #first name is the part of the players name upto the first space
last_name = player[player.find(' ')+1:]              #last name is the part of the players name after the first space
last_name_len = len(player[player.find(' ')+1:]) 

name_short = first_name[0] +'. ' + last_name

chant = (len(first_name) * str(f'{first_name}! '))[:-1]

print(chant)

good_chant = chant[-1:] != ' '