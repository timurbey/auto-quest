from auto_quest.dummy import DummyCharacter

def main():
    characters = [DummyCharacter(name = 'dummy1', health = 10)]
    done = False
    while not done:
        for character in characters:
            character.act(characters)

if __name__ == '__main__':
    main()
