import sys


from webapp.main import run_app, load_config


def run(argv):
    config = load_config(argv)
    run_app(argv)


if __name__ == '__main__':
    run(sys.argv[1:])