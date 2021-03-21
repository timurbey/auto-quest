from auto_quest.dummy import dummy_battle

def print_summary(turns, winners):
    print('battle length: ' + str(turns) + ' turns')
    print('winning team:')
    print(winners)

def ffa(character_count = 10, rounds = 1):
    for i in range(rounds):
        print('round ' + str(i + 1) + ':')
        print_summary(*dummy_battle(character_count))

def team_fight(character_count = 10, team_count = 2, rounds = 1):
    if character_count % team_count != 0:
        raise Exception(str(character_count) + ' characters not divisible into ' + str(team_count) + ' teams')

    team_size = character_count // team_count
    for i in range(rounds):
        print('round ' + str(i + 1) + ':')
        print_summary(*dummy_battle(team_size, team_count))

def main():
    ffa(50, rounds = 10)
    team_fight(12, 3, rounds = 10)

if __name__ == '__main__':
    main()
