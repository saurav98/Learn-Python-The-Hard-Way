from sys import exit

def gold_room():
    print "This room is full of gold. How much would you like take?"

	
    next = (raw_input("> "))
    how_much = next.split(" ")
    nums = []
    n = 0
    while n < 10000:
        nums.append(n)
        n = n + 1		
    i = 0	
    ngold = []
    print len(how_much)
    while i < len(how_much):
        for num in nums:
             
            if str(num) == how_much[i]:
                ngold.append(num)
        i = i + 1
     
    x = len(ngold)
    print ngold
    if x == 0:
        print "Man learn to type a number."
    elif int(ngold[0]) < 50:		
	    
        
            print "Nice, you are not greedy, you win!"
    else:
        dead("You greedy bastard!")

		
		
def bear_room():
    print """    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door .
    How are you going to move the bear ?"""
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not  bear_moved:
            print "The bear has moved from the door . You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed of and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means. "


def cthulhu_room():
    print """    Here you see the great evil Cthulhu.			
    He, it , whatever stares at you and you go insane.
    Do you flee for your life or eat your head?"""

    next = raw_input("> ")
	
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)
	
	
def start():
    print """    You are in a dark room.
    There is a door to your right and left.
    Which one do you take?"""
	
    next == raw_input()

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve.")

start()		