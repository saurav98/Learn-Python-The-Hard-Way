print """
Let's play hand cricket.
For rules type rules().
"""
def rules():
    print """1. Player 1 bats first.
    2. Player has to choose no fom 1 to 6	
    3. If both player choose the same number 
    than batsman is out.
    4. Tf not then the number is added to the batsman total."""
	
player1 = raw_input("Player 1's name => ")
player2 =raw_input("Player 2's name => ")

print "Let us the start match."

c = "Choose a number from 1 to 6."
out = "%r is out."% player1
runs = "Player scored %r runs"   
total_score = "%r's total score is %r."

score = 0

num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player1, score)

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player1, score)	

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player1, score)

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player1, score)


num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player1, score)

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player1, score)	


	
	



	
print "%r 's innings is over."%player1
print total_score% (player1, score)

target = score + 1

print "Target for %r is %r."% (player2, target)





	
score = 0

	


out = "%r is out."% player2
	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player2, score)

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player2, score)

num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player2, score)

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player2, score)	

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player2, score)

	
num1 = int(raw_input(c))
num2 = int(raw_input(c))
if num1 == num2 :
    print out
elif num1!= num2:
    score = score + num1 
    print runs %(num1)
    print total_score % (player2, score)

	
print "%r 's innings is over."%player2
print total_score% (player1, score)

	
print "%r's innings is over."
print total_score% (player2, score)

if target >= score:
    print "%r has won the game" %(player1)
elif target -1 == score:
    print "Game is tied between %r and %r." %(player1, player2)
else:
    print "%r has won the game" % (player2)
	
	
raw_input("Press any key to exit.")
