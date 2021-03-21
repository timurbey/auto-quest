from random import choice

from auto_quest import Affiliation, Battle
from auto_quest.dummy import DummyCleric
from auto_quest.dummy import DummyFighter
from auto_quest.dummy import DummyMage
from auto_quest.dummy import DummyThief

DUMMY_PARTY_CHOICES = [DummyCleric, DummyFighter, DummyThief, DummyMage]

def dummy_party(count = 10):
    return [choice(DUMMY_PARTY_CHOICES)() for _ in range(count)]

def battle_royal(teams):
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
        aff, battle_log = battle_royal(dummy_party(team_size))
    else:
        aff, battle_log = battle_royal([dummy_party(team_size) for _ in range(team_count)])

    battle_end = battle_log[-1][-1]
    for c in battle_end:
        if c['health'] > 0:
            winners = aff.of(c['id'])
            break
    return len(battle_log), [(c['id'], c['name'], c['class']) for c in battle_end if aff.of(c['id']) == winners]
