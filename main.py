import time
import os

os.environ['P_MaxHP'] = '50'
os.environ['P_CurrentHP'] = '45'
os.environ['P_Gold'] = '15'

TitleTB = '+==============+'
TitleN =  '|   The Echo   |'

def clear():
    os.system('clear')


def title():
    print(TitleTB)
    print(TitleN)
    print(TitleTB)


def options():
    print('    New Game    ')
    print('      Quit      ')


MM = True

while MM == True:
    clear()
    title()
    options()
    print()
    Choice = input('Option> ').lower()

    if Choice in {'quit', 'exit'}:
        os.close(0)
    elif Choice in {'new', 'new game'}:
        MM = False
    else:
        clear()
        print('Incorrect choice, please choose a valid option.')
        time.sleep(2)

os.system('python Levels/R1.py')