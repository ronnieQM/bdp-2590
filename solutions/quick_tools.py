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
    time.sleep(1.5)
    print('\nbye\n')
    time.sleep(1)
    exit()


def yellll():
    print('$%*#!!!!  ' * 10)
    print('LOOK HERE:')


def tbd():
    tabs = '  '
    count = 0
    for i in range(0, 4):
        print(i)
        ntabs = tabs * count
        count += 1
        print(ntabs, '└', i)
