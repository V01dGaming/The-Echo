import time
import os
import random

def clear():
    os.system('clear')

MaxHP = os.environ['P_MaxHP']
HP = os.environ['P_CurrentHP']
Gold = os.environ['P_Gold']


NewHP = int(HP)
R2 = True
    
while R2 == True:
    clear()
    print('HP: ' + HP + '/' + MaxHP)
    print('Gold: ' + Gold)
    print()
    print()
    time.sleep(1)