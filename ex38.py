ten_things = "Apples Oranges Crows Telephone Light Sugar"

print 'Wait there\'s not things in that list, let\'s fix that.'

stuff = ten_things.split(" ")
more_stuff = "Day Night Song Frisbee Corn Banana Girl Boy  "

more_stuff = more_stuff.split(" ")

i = len(stuff)
 
	

print "=============================="

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding:", next_one	
    stuff.append(next_one)
print "There is %d items now." % len(stuff)

print """

#####################

"""
print "printing pop()"
print more_stuff.pop()
print "printing pop(2)"
print """
%r 
"""% more_stuff.pop(2)
for i in range(3):
    next_one = more_stuff[i]
    print "Adding: " , next_one
    stuff.append(next_one)
    print "There's {0} items now".format(len(stuff))

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[0]
print stuff[-1]#whoa! fancy
print stuff.pop()
print "@".join(stuff)#what? cool 
print "#".join(stuff[3:6])#super stellar!
print more_stuff    

    
def temp():
    print "cheking for issue."
    print "Sucessfull "
	

