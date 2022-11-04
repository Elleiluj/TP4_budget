import os
import sys


def main():
    # Cherche les paramètres (hash des commits) dans l'appel du script
    args = sys.argv[1:]

    os.system('git bisect start %s %s' % (args[0], args[1]))
    os.system('git bisect run python manage.py test')
    os.system('git bisect reset')


if __name__ == '__main__':
    main()

