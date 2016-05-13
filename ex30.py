people = int(raw_input('people---->'))
cars = int(raw_input('cars---->'))
buses = int(raw_input('buses---->'))




if cars > people:
    print "We could take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
	
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."
	
if people > buses:
    print "Alreight , let's just take the buses."
else:
    print "Fine, let's stay home then."
	
