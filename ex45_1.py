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
            print "You have qualified for level2"
            Level2(5)
        else:
            sau = AddOns()
            sau.exit()
            
class AddOns(object):
    def exit():
        exit_msg = ["You're trying to say you like DOS better than me, right?",
                    "Ya know, next time you come in here I'm gonna toast ya."]
        print random.choice(exit_msg)          
                    
    def quit():
        quit_msg = [
                    "Please don't leave, there's more demons to toast!",
                    "Don't leave yet -- There's a demon around that corner!",
                    "Go ahead and leave. See if I care.",
                    "Are you sure you want to quit this great game?",
                    "You're lucky I don't smack you for thinking about leaving."]
        print random.choice(quit_msg)             
                    
    def life():
        pass
    def rules():
        pass
    def score():
        pass
    
Play()
