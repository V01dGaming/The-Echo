import time
import os

TitleTB = '+==============+'
TitleN = '|   The Echo   |'

def Clear():
    os.system('clear')

def Options():
    print('    NEW GAME')
    print('      QUIT')
    print()


def Title():
    print(TitleTB)
    print(TitleN)
    print(TitleTB)

MM = True

while MM == True:
    Clear()
    Title()
    Options()

    Choice = input('Choice> ').lower()

    if Choice in {'new', 'new game'}:
        MM = False
    else:
        Clear()
        print('No')
        time.sleep(2)

os.system('python Game/Start.py')