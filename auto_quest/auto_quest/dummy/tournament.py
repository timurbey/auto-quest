from auto_quest.dummy import dummy_battle

def check_teams(character_count, team_count):
    if character_count % team_count != 0:
        raise Exception(str(character_count) + ' characters not divisible into ' + str(team_count) + ' teams')

# TODO(timur): this is not very informative currently
def get_battle_end(aff, log):
    end = log[-1][-1]
    for c in end:
        if c['health'] > 0:
            winners = aff.of(c['id'])
            break
    return len(log), [(c['id'], c['name'], c['class']) for c in end if aff.of(c['id']) == winners]

def print_summary(turns, winners):
    print('battle length: ' + str(turns) + ' turns')
    print('winning team:')
    print(winners)

def ffa(character_count = 10, rounds = 1):
    for i in range(rounds):
        print('round ' + str(i + 1) + ':')
        print_summary(*get_battle_end(*dummy_battle(character_count)))

def team_fight(character_count = 10, team_count = 2, rounds = 1):
    check_teams(character_count, team_count)
    team_size = character_count // team_count
    for i in range(rounds):
        print('round ' + str(i + 1) + ':')
        print_summary(*get_battle_end(*dummy_battle(team_size, team_count)))

def run_dummy_tournament(character_count = 50, team_count = 10, rounds = 10):
    check_teams(character_count, team_count)
    ffa(character_count = character_count, rounds = rounds)
    team_fight(character_count = character_count, team_count = team_count, rounds = rounds)
