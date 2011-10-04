#!/usr/bin/python

from bb_score_objects import *

phillies = Team(name="Phillies", hometown="Philadelphia", manager="Charlie Manuel", league="NL")
jason = Player(phillies, "Jason Bachman", 99, 1, "L", "L")
jason_id = jason.lookup_player_id()
print jason.name, ":", jason_id

lee = Player(phillies, "Cliff Lee", 33, 1, "L", "L")
lee_id = lee.lookup_player_id()
print lee.name, ":", lee_id
