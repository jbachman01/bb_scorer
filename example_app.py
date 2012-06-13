#!/usr/bin/python

from bb_score_objects import *

# set up teams
phillies = Team(name="Phillies", hometown="Philadelphia", manager="Charlie Manuel", league="NL")
braves = Team(name="Braves", hometown="Atlanta", manager="Bobby Cox", league="NL")

# Phillies players
lee = Player(phillies, "Cliff Lee")
ruiz = Player(phillies, "Carlos Ruiz")
howard = Player(phillies, "Ryan Howard")
utley = Player(phillies, "Chase Utley")
martinez = Player(phillies, "Michael Martinez")
rollins = Player(phillies, "Jimmy Rollins")
ibanez = Player(phillies, "Raul Ibanez")
victorino = Player(phillies, "Shane Victorino")
mayberry = Player(phillies, "John Mayberry")
lineup_away_110926 = Lineup(team=phillies, one=rollins, two=utley, three=mayberry, four=howard, five=victorino, six=ibanez, seven=martinez, eight=ruiz, nine=lee)

# Braves players
bourn = Player(braves, "Michael Bourn")
prado = Player(braves, "Martin Prado")
jones = Player(braves, "Chipper Jones")
uggla = Player(braves, "Dan Uggla")
freeman = Player(braves, "Freddie Freeman")
mccann = Player(braves, "Brian McCann")
diaz = Player(braves, "Matt Diaz")
gonzalez = Player(braves, "Alex Gonzalez")
delgado = Player(braves, "Randall Delgado")
lineup_home_110926 = Lineup(team=braves, one=bourn, two=prado, three=jones, four=uggla, five=freeman, six=mccann, seven=diaz, eight=gonzalez, nine=delgado)

# set up game
phillies_braves_110926 = Game("110926", braves, lineup_home_110926, phillies, lineup_away_110926)

# print out game and lineup info
phillies_braves_110926.game_info()
lineup_away_110926.lineup_info()
lineup_home_110926.lineup_info()

# save game data to xml
phillies_braves_110926.save_to_xml()


