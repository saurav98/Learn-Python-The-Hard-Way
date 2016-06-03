import sys
import random

class Level(object):
    def __init__(self, evil_life):
        self.evil_life = evil_life
        i = 5
        while i > 0 and evil_life > 0:
            player = raw_input("> ")
            evil = random.randint(0, 5)
            
            if evil_life <= 0:
                i -= 1
            elif evil == player:
                evil_life = evil_life - 3
                i -= 1
            elif (evil == evil_life + 1 )or (evil == evil_life - 1):
                evil_life = evil_life - 1
                i -= 1
            elif player == "quit":
                sau = AddOns()
                sau.quit()
            elif player == "rules" :
                sau = AddOns()
                sau.rules()
            elif player == "life":
                sau = AddOns()
                sau.life()
            elif player == "status":
                sau = AddOns()
                sau.status()
            else:
                i -= 1
        if evil_life <= 0:
            global result 
            result = "qualifed"
        else:
            global result
            result = "failed"
        
 
     
class Level1(Level):
    pass


class Level2(Level):
    pass

class AddOns(object):
    
    def exit(self):
        exit_msg = ["You're trying to say you like DOS better than me, right?",
                    "Ya know, next time you come in here I'm gonna toast ya."]
        print random.choice(exit_msg)          
                    
    def quit(self):
        quit_msg = [
                    "Please don't leave, there's more demons to toast!",
                    "Don't leave yet -- There's a demon around that corner!",
                    "Go ahead and leave. See if I care.",
                    "Are you sure you want to quit this great game?",
                    "You're lucky I don't smack you for thinking about leaving."]
        print random.choice(quit_msg)             
                    
    def life(self):
        print "You have %r life left" %life_left
    
    def rules(self):
        print "This is games rules."
    
    def status(self):
        print "You have %r life left" %life_left
        print "You are in level %r" %level      
        
class Play(object):
    def __init__(self):
        global level
        level = 1
        Level1(3)
        if result == "qualifed":
            global level
            level = 2
            print "You have qualified for level2"
            Level2(5)
        else:
            sau = AddOns()
            sau.exit()
            
        
    
life_left = 3    

while life_left > 0:
    print "You have %r life left" %life_left
    Play()
    life_left -= 1
