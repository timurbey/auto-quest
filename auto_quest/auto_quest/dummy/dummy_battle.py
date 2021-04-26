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

def dummy_battle(team_size, team_count = None, rounds = 1):
    if team_count is None:
        aff, battle_log = setup_battle(dummy_party(team_size))
    else:
        aff, battle_log = setup_battle([dummy_party(team_size) for _ in range(team_count)])

    battle_end = battle_log[-1][-1]
    for c in battle_end:
        if c['health'] > 0:
            winners = aff.of(c['id'])
            break
    return len(battle_log), [(c['id'], c['name'], c['class']) for c in battle_end if aff.of(c['id']) == winners]
