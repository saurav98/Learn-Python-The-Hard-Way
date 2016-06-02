import sys
import random

class EvilLife(object):
    def life(self):
        return 10

class Level(object):
    
    
    def __init__(self):
        foo = EvilLife()
        life = foo.life()
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
            result = "qualifed"
        else:
            result = "fail"
            
        print result
class Level1(Level):
    pass
    
class level2(Level):
    pass

class Map(object):
    
    
    
