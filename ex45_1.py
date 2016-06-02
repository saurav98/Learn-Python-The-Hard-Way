import sys
import random

life = 10

class Engine(object):
    opening_level = level1
    

class Level(object):
    def __init__(self, life):
        self.life = life
        
        for i in range (5):
            player = raw_input("> ")
            evil = random.randint(0, 5)
            
            if life <= 0:
                pass
            elif evil == player:
                life = life - 3
            elif (evil == life + 1 )or (evil == life - 1):
                life = life - 1
            else:
                pass
        if life <= 0:
            global result 
            result = "qualifed"
        else:
            global result
            result = "fail"
            
        print "You have %s" %result
    return result
class Level1(Level):
    pass
class level2(Level):
    pass

class Map(object):
    if Level1 == "qualified":
        pass
    
    
