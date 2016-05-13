print """
Let's play hand cricket.
For rules type rules().
"""
def rules():
    print """1. Player 1 bats first.
    2. Player has to choose no fom 0 to 6	
    3. If both player choose the same number 
    than batsman is out.
    4. Tf not then the number is added to the batsman total."""

player1 = raw_input("Player 1's name > ")
player2 = raw_input("Player 2's name > ")
	
overs = int(raw_input('How much overs would you like to play? > '))

raw_input("Are you ready?")

score = 0
i = 1
while i <= overs*6:
    print "Over:  ",i/6+1,'.',i-1
    bat =  int(raw_input(player1 + " > "))
    ball =  int(raw_input(player2 +" > "))
    if   0 > bat or bat > 6:
        print '%r commited a foul.' % player1
        print "Type rules() for help."
        print "%r's total score is %r" %(player1, score)		
        i = i + 1 
    elif bat == ball:
        print "%r is out."%(player1)
        print "%r's total score is %r."%(player1, score)
        i = overs*6 +1	
		
    else:
        score = score + bat	    
        print "%r scored %r runs." %(player1, bat)
        print "%r's total score is %r" %(player1, score)
        i = i + 1		
		
		
print "%r now has to defend %r "%(player1, score)

target = score + 1

print "%r has to score %r runs to win."%(player2, target)






score = 0
i = 1
while i <= overs*6:
    print "Over:  ",i/6+1,'.',i-1
    bat =  int(raw_input(player2 + " > "))
    ball =  int(raw_input(player1 +" > "))
    if   (0 > bat or bat > 6) and score < target:
        print '%r commited a foul.' % player2
        print "Type rules() for help."
        print "%r's total score is %r" %(player2, score)		
        i = i + 1 
    elif bat == ball  and score < target:
        print "%r is out."%(player2)
        print "%r's total score is %r."%(player2, score)
        i = overs*6 +1	
       		
    elif bat!= ball and score < target:
        score = score + bat	    
        print "%r scored %r runs." %(player2, bat)
        print "%r's total score is %r" %(player2, score)
        i = i + 1		
    elif  score > target:
        print "%r wins this game."%player2
    else:
        i = i + 1

if score == target - 1:
    print "Match is Tied between %r and %r."%(player1, player2)
else: 
    print "%r has won this match."%(player1)


raw_input("Press any key to exit")	







