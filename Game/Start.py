import time
import os
from decouple import config

def Clear():
    os.system('clear')


Meep = config('PLAYERMAXHEALTH')

Clear()
print(Meep)