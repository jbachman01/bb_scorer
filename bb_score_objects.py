#!/usr/bin/python
"""
bb_scorer
"""

from lxml import etree 

def trans_position(pos_num):
    """ take a positions number and return a position name """
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

class Player(object):
    """ a baseball player """
    def __init__(self, team, name='', number='', pos_num='', bats='', throws=''):
        self.name = name
        self.number = number
        self.pos_num = pos_num
        self.bats = bats
        self.throws = throws

    def player_info(self):
        print('{:<20}{:<8}{:<15}'.format("Name:", "Number:", "Position:"))
        print('{:<20}{!s:<8}{:<15}'.format(self.name, self.number, trans_position(self.pos_num)))
        #print self.name + " (" + str(self.number) + ") - " + trans_position(self.pos_num)

    def player_xml(self, parent_el):
        no_space_name = self.name.replace(' ', '_')
        return etree.SubElement(parent_el, no_space_name, name=self.name, number=str(self.number), position=str(self.pos_num), bats=self.bats, throws=self.throws)

class Team(object):
    """ a baseball team """
    def __init__(self, name='', hometown='', manager='', league=''):
        self.name = name
        self.hometown = hometown
        self.manager = manager
        self.league = league

class Lineup(object):
    """ a team's current lineup """
    def __init__(self, team, one, two, three, four, five, six, seven, eight, nine, DH=''):
        self.team = team
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        if self.team.league == 'AL':
            self.dh = DH

    def lineup_info(self):
        print("  " + '{:<20}{:<8}{:<15}'.format("Name:", "Number:", "Position:"))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("1", self.one.name, self.one.number, trans_position(self.one.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("2", self.two.name, self.two.number, trans_position(self.two.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("3", self.three.name, self.three.number, trans_position(self.three.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("4", self.four.name, self.four.number, trans_position(self.four.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("5", self.five.name, self.five.number, trans_position(self.five.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("6", self.six.name, self.six.number, trans_position(self.six.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("7", self.seven.name, self.seven.number, trans_position(self.seven.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("8", self.eight.name, self.eight.number, trans_position(self.eight.pos_num)))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("9", self.nine.name, self.nine.number, trans_position(self.nine.pos_num)))

    def lineup_xml(self, game_xml, lineup_name):
        lineup_xml = etree.SubElement(game_xml, lineup_name, team=self.team.name)
        one = self.one.player_xml(lineup_xml)
        two = self.two.player_xml(lineup_xml)
        three = self.three.player_xml(lineup_xml)
        four = self.four.player_xml(lineup_xml)
        five = self.five.player_xml(lineup_xml)
        six = self.six.player_xml(lineup_xml)
        seven = self.seven.player_xml(lineup_xml)
        eight = self.eight.player_xml(lineup_xml)
        nine = self.nine.player_xml(lineup_xml)
        return lineup_xml

class Game(object):
    """ a game between two teams """
    def __init__(self, date, home_team, home_lineup, away_team, away_lineup):
        self.date = date
        self.home_team = home_team
        self.home_lineup = home_lineup
        self.away_team = away_team
        self.away_lineup = away_lineup

    def game_info(self):
        print(self.away_team.name + " at the " + self.home_team.name + " (" + self.date + ")")

    def save_to_xml(self):
        game_xml = etree.Element("game")
        home_lineup_el = self.home_lineup.lineup_xml(game_xml, lineup_name="home_lineup")
        away_lineup_el = self.away_lineup.lineup_xml(game_xml, lineup_name="away_lineup")
        filename = "./" + self.home_team.name + self.away_team.name + self.date + ".xml"
        try:
            game_xml_file = open(filename, "w")
            game_xml_file.write(etree.tostring(game_xml, pretty_print=True))
            game_xml_file.close()
        except IOError:
            print("Can not open file: " + filename)

class AtBat(object):
    """ a player's at bat """
    def __init__(self, player, action, destination):
        self.player = player
        self.action = action
        self.destination = destination
