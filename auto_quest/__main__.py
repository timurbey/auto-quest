from auto_quest import AutoBattle
from auto_quest.dummy import *

def main():
    characters = []
    for affiliation in range(2):
        characters.append(DummyCleric(affiliation = affiliation % 2))
        characters.append(DummyFighter(affiliation = affiliation % 2))
        characters.append(DummyMage(affiliation = affiliation % 2))
        characters.append(DummyThief(affiliation = affiliation % 2))
    log = AutoBattle(characters).run()
    print(log[-1][0])
    [print(c) for c in log[-1][-1]]
    # print(len(log))

if __name__ == '__main__':
    main()
