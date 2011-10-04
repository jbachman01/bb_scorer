#!/usr/bin/python

from bb_score_objects import *

phillies = Team(name="Phillies", hometown="Philadelphia", manager="Charlie Manuel", league="NL")
lee = Player(phillies, "Cliff Lee", 33, 1, "L", "L")
lee_id = lee.lookup_player_id()
print lee_id
