import sys
import random

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
     
class Level1(Level):
    pass
class Level2(Level):
    pass

class Play(object):
    def __init__(self):
        Level1(3)
        if result == "qualifed":
            print "Hi"
            Level2(5)
        else:
            print "your game is over"
    
Play()
