#!/usr/bin/python

import team, db

team_kwargs = {'team_id': 143}
# phils = team.Team(team_kwargs)
# phils.loadRoster()
# phils.save()
db_connection = db.DB()
roster_40 = list(db_connection.query(['name_display_first_last', 'primary_position_txt', 'era', 'avg'], 'player', 'team_id', '143'))
db_connection.close()
pitchers = ['{0:<20} ({1}): {2}'.format(name, pos, era) for name, pos, era, avg in sorted(roster_40, key=lambda x: x[0]) if pos == 'P']
print "Pitchers:"
for pitcher in pitchers:
    print pitcher
