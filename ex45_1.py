import sys
import random


class Level(object):
    def life():
        global life
        life = 10
    
    def __init__(self):
        for i in range (5):
            player = raw_input("> ")
            evil = random.randint(0, 5)
            
            if life <= 0:
                pass
            elif evil == player:
                life = life - 3
            elif (evil = life + 1 )or (evil = life - 1):
                life = life - 1
            else:
                pass
        if life <= 0:
            "qualifed"
        else:
            "fail"
            
                
class Level1(Level):
    pass
    
class level2(Level):
    def life():
        global life
        life = 15
            
class level3(Level)
    def life():
        global life
        life = 20
    
    
