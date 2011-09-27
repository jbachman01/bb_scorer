#!/usr/bin/python

from bb_score import *

phillies = Team(name="Phillies", hometown="Philadelphia", manager="Charlie Manuel", league="NL")
braves = Team(name="Braves", hometown="Atlanta", manager="Bobby Cox", league="NL")

# Phillies players
lee = Player(phillies, "Cliff Lee", 33, 1, "L", "L")
ruiz = Player(phillies, "Carlos Ruiz", 51, 2, "R", "R")
howard = Player(phillies, "Ryan Howard", 6, 3, "L", "L")
utley = Player(phillies, "Chase Utley", 26, 4, "L", "R")
martinez = Player(phillies, "Michael Martinez", 19, 5, "S", "R")
rollins = Player(phillies, "Jimmy Rollins", 11, 6, "S", "R")
ibanez = Player(phillies, "Raul Ibanez", 29, 7, "L", "R")
victorino = Player(phillies, "Shane Victorino", 8, 8, "S", "R")
mayberry = Player(phillies, "John Mayberry", 15, 9, "R", "R")
lineup_away_110926 = Lineup(team=phillies, one=rollins, two=utley, three=mayberry, four=howard, five=victorino, six=ibanez, seven=martinez, eight=ruiz, nine=lee)

# Braves players
bourn = Player(braves, "Michael Bourn", 24, 8, "L", "R")
prado = Player(braves, "Martin Prado", 14, 7, "R", "R")
jones = Player(braves, "Chipper Jones", 10, 5, "S", "R")
uggla = Player(braves, "Dan Uggla", 26, 4, "R", "R")
freeman = Player(braves, "Freddie Freeman", 5, 3, "L", "R")
mccann = Player(braves, "Brian McCann", 16, 2, "L", "R")
diaz = Player(braves, "Matt Diaz", 23, 9, "R", "R")
gonzalez = Player(braves, "Alex Gonzalez", 2, 6, "R", "R")
delgado = Player(braves, "Randall Delgado", 40, 1, "R", "R")
lineup_home_110926 = Lineup(team=braves, one=bourn, two=prado, three=jones, four=uggla, five=freeman, six=mccann, seven=diaz, eight=gonzalez, nine=delgado)

phillies_braves_110926 = Game("110926", braves, lineup_home_110926, phillies, lineup_away_110926)

phillies_braves_110926.game_info()
lineup_away_110926.lineup_info()
lineup_home_110926.lineup_info()

phillies_braves_110926.save_to_xml()


