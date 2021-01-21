from auto_quest import Character

def main():
    characters = [Character(name = 'dummy1', health = 10)]
    done = False
    while not done:
        for character in characters:
            done = done or character.act(characters)

if __name__ == '__main__':
    main()
