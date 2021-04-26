from argparse import ArgumentParser
from auto_quest.dummy import run_dummy_tournament

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--dummy', action='store_true')
    return parser.parse_args()

def main():
    args = parse_args()

    # TODO(timur): add hooks for custom logic
    if args.dummy:
        run_dummy_tournament()

if __name__ == '__main__':
    main()
