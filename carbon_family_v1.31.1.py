print """
Welcome to Kanchan Tutorial 
In this session i will test your knownledge on
CARBON FAMILY
"""

ans = int(raw_input("How much isotopes carbon have? > " ))

c = "Your ans is correct."
w = "Your ans is wrong."

if ans == 3:
    print c
    points = 1
    ans = raw_input("Can you name theme? > ")
    x = ans.split(" ")
    print """
	Your response: %r
    Correct answer is: c12, c13, c14""" % x	
    ans = raw_input("Can you guess which one is radioactive? > ")
    if ans == "c14":
        print c	
    else:
    	print w
    ans = int(raw_input("What is the half life (in years) of c14? > "))
    if 5700 <= ans <= 5800:
        print c
    		
    else :
        print w
        print "It is 5770 years"	
else:
    print w

raw_input("Press any key to exit.")
   