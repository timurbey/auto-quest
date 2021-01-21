def main():
    actors = [
        {
            'name': 'dummy1',
            'health': 10,
            'actions': []
        }
    ]
    done = False
    while not done:
        for actor in actors:
            done = done or actors.act(actor, actors)

if __name__ == '__main__':
    main()
