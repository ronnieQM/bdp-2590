import time
import sys
import os


def waitr():
    try:
        raw_input('. . . . . . . . .')
    except:
        input('. . . . . . . . . . .')


def breakpoint():
    x = '. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .'
    try:
        while True:
            for i in x:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(3)
    except KeyboardInterrupt:
        pass


def clearit():
    os.system('cls' if os.name == 'nt' else 'clear')


def breakout():
    print('\nbye\n')
    time.sleep(1)
    exit()
