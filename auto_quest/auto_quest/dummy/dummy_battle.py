from random import choice

from auto_quest.dummy import Affiliation, Battle
from auto_quest.dummy import Cleric, Fighter, Mage, Thief

DUMMY_PARTY_CHOICES = [Cleric, Fighter, Mage, Thief]

def dummy_party(count = 10):
    return [choice(DUMMY_PARTY_CHOICES)() for _ in range(count)]

def setup_battle(teams):
    team_ids = range(len(teams))
    try:
        team_ids = {c.id: i for team, i in zip(teams, team_ids) for c in team}
        teams = [c for team in teams for c in team]
    except:
        team_ids = dict(zip((c.id for c in teams), team_ids))
    aff = Affiliation(team_ids)
    battle = Battle(teams, aff)
    return aff, battle.run()

def dummy_battle(team_size, team_count = None):
    if team_count is None:
        return setup_battle(dummy_party(team_size))
    else:
        return setup_battle([dummy_party(team_size) for _ in range(team_count)])
