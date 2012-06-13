#!/usr/bin/python
"""
bb_scorer
"""

from lxml import etree 
import urllib2
import re
import json
import py_mlb.player
import pprint

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

class Player(py_mlb.player.Player):
    #from py_mlb import player

    """ a baseball player 
    Inherets from py_mlb.player.Player which gives these keys:
    'active_sw'
    'bats'
    'birth_city'
    'birth_country'
    'birth_date'
    'file_code'
    'gender'
    'height_feet'
    'height_inches'
    'high_school'
    'jersey_number'
    'name_display_first_last'
    'name_display_first_last_html'
    'name_display_last_first'
    'name_display_last_first_html'
    'name_display_roster'
    'name_display_roster_html'
    'name_first'
    'name_full'
    'name_last'
    'name_middle'
    'name_use'
    'player_id'
    'primary_position'
    'primary_position_txt'
    'primary_sport_code'
    'pro_debut_date'
    'start_date'
    'status'
    'status_code'
    'status_date'
    'team_abbrev'
    'team_code'
    'team_id'
    'team_name'
    'throws'
    'weight'

    """
    def __init__(self, team, name=None):
        self.name = name
        player_id = self.lookup_player_id()
        super(Player, self).__init__(player_id)

    def player_info(self):
        print('{:<20}{:<8}{:<15}'.format("Name:", "Number:", "Position:"))
        print('{:<20}{!s:<8}{:<15}'.format(self.name, self.number, trans_position(self.pos_num)))
        #print self.name + " (" + str(self.number) + ") - " + trans_position(self.pos_num)

    def player_xml(self, parent_el):
        no_space_name = self.name.replace(' ', '_')
        return etree.SubElement(parent_el, no_space_name, name=self.name, number=str(self["jersey_number"]), position=str(self["primary_position"]), bats=self["bats"], throws=self["throws"])

    def lookup_player_id(self):
        req = urllib2.Request('http://mlb.mlb.com/lookup/json/named.search_autocomp.bam?sport_code=%27mlb')
        res = urllib2.urlopen(req)
        content = res.read()
        content = re.sub('\/\*.+?\*\/', '', content)
        obj = json.loads(content)
        player_rows = obj["search_autocomp"]["search_autocomplete"]["queryResults"]["row"]
        search_name = self.name.lower()
        player_id = None
        try:
            for pl in player_rows:
                if search_name == str(pl["n"]).lower():
                    player_id = str(pl["p"])
            if player_id:
                return player_id
            else:
                raise PlayerLookupError(self.name)
        except PlayerLookupError as e:
            print 'Could not find player id for', e.value 


class PlayerLookupError(Exception):
    """ error to throw when a player's id cannot be found """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Team(object):
    """ a baseball team """
    def __init__(self, name=None, hometown=None, manager=None, league=None):
        self.name = name
        self.hometown = hometown
        self.manager = manager
        self.league = league

class Roster(object):
    """ all active player's on a team """
    def __init__(self, team):
        self.team = team

class Lineup(object):
    """ a team's current lineup """
    def __init__(self, team, one, two, three, four, five, six, seven, eight, nine, DH=None):
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
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("1", self.one.name, self.one["jersey_number"], self.one["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("2", self.two.name, self.two["jersey_number"], self.two["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("3", self.three.name, self.three["jersey_number"], self.three["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("4", self.four.name, self.four["jersey_number"], self.four["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("5", self.five.name, self.five["jersey_number"], self.five["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("6", self.six.name, self.six["jersey_number"], self.six["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("7", self.seven.name, self.seven["jersey_number"], self.seven["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("8", self.eight.name, self.eight["jersey_number"], self.eight["primary_position_txt"]))
        print('{:<2}{:<20}{!s:<8}{:<15}'.format("9", self.nine.name, self.nine["jersey_number"], self.nine["primary_position_txt"]))

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

