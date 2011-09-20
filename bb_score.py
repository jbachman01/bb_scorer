#!/usr/bin/python
"""
bb_scorer
"""

class Team(object):
    """ a baseball team """
    def __init__(self, name='', hometown='', manager=''):
        self.name = name
        self.hometown = hometown
        self.manager = manager

class Player(Team):
    """ a baseball player """
    def __init__(self, name='', number='', pos_num='', throws='', bats=''):
        self.name = name
        self.number = number
        self.pos_num = pos_num

    def player_info(self):
        print "Name: " + self.name
        print "Number: " + str(self.number)
        print "Position: " + self.trans_position(self.pos_num)

    def trans_position(self, pos_num):
        positions = {1: 'Pitcher', 
                2: 'Catcher', 
                3: 'First Base', 
                4: 'Second Base', 
                5: 'Third Base', 
                6: 'Shortstop', 
                7: 'Left Field', 
                8: 'Center Field', 
                9: 'Right Field', 
                'DH': 'Designated Hitter'} 
        return positions[pos_num]

