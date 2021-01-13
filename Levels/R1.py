import time
import os
import random

def clear():
    os.system('clear')

MaxHP = os.environ['P_MaxHP']
HP = os.environ['P_CurrentHP']
Gold = os.environ['P_Gold']


NewHP = int(HP)
R1 = True
    
while R1 == True:
    clear()
    print('HP: ' + HP + '/' + MaxHP)
    print('Gold: ' + Gold)
    print()
    print()
    print("You wake up in a dark, damp cave. You don't know how you got there and you feel a sharp pain in your arm, a rock is sticking out. The cut is bleeding. What do you do?")
    print()
    print('Please enter the number.')
    print('1) Remove the rock in your arm |Skill Check|')
    print('2) Wait to go to a doctor')
    print()
    Room = input('Choice> ')
    
    if Room == '1':
        Chance = random.randint(0, 100)
        if Chance in range(50, 100):
            NewHP = NewHP + 5
            HP = str(NewHP)
            clear()
            print()
            print('Skill Check Success')
            print()
            print('You removed the rock and covered the cut with a piece of cloth, luckly the cut wasnt a major wound.')
            print()
            print('Your Health is now ' + HP + '/' + MaxHP)
            time.sleep(5)
            R1 = False
        else:
            NewHP = NewHP - 5
            HP = str(NewHP)
            clear()
            print()
            print('Skill Check Failed')
            print()
            print("You removed the rock, but couldn't find any cloth. Your wound is bleeding.")
            print()
            print("You decide to proceed in to the cave, hoping you'll fand a doctor outside.")
            print()
            print('Your Health is now ' + HP + '/' + MaxHP)
            time.sleep(5)
            R1 = False
            
    elif Room == '2':
        NewHP = 0
        if NewHP == 0:
            clear()
            print('You died due to blood loss')
            print()
            print("Time to pay respects")
            time.sleep(5)
            os.close(0)
            
    
    else:
        clear()
        print('Please choose another option')
        time.sleep(2)

os.environ['P_MaxHP'] = MaxHP
os.environ['P_CurrentHP'] = HP
os.environ['P_Gold'] = Gold
os.system('python Levels/R2.py')