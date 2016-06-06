import sys
import random

global life_left
global run_level
global level_left

class Engine(object):
    def __init__(self, level_map):
        self.level_map = level_map
        level_map

    def play(self, opening_level):
        global life_left
        life_left = 3
        while life_left > 0:
            self.level_map
            self.level_map.next_level()
            life_left -= 1


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
 

class Level1(Level):
    global level
    level = 1


class Level2(Level):
    global level
    level = 2


class Map(object):
    global run_level
    run_level = level + 1
    
    def __init__(self, opening_level):
        self.opening_level = opening_level

    def next_level(self):
        if run_level == "qualified":
            eval("Level" + (level+1) + (3))
        else:
            sau = AddOns()
            sau.exit()


a_map = Map(Level1(3))
a_game = Engine(a_map)
a_game.play(a_map)
