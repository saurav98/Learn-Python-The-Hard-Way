print "How smart are you really ?"
print "Put your knowledge to the test with this iq test "
print "based on real iq test questions." 




raw_input("Hit enter to continue.")

questions = ["What goes up and never comes down?", "What has a head and a tail but no body?", "A is the father of B. But B is not the son of A. How's that possible", "Spell 'Ghost' out loud. Then spell 'Most' out loud. Then spell 'Roast' out loud. What do you put in a toaster?", "How do you walk on water?", "Name the most recent year in New year's came before christmas? ","10 copycats were sitting in a boat 1 jumped out how many left?", "How many sides does a circle have?", "A cowboy rode to an inn on Friday. He stayed two nights and left on Friday. How could that be?", "What familiar word starts with 'is', ends with 'and', snd has la in the middle?" ]


anskey = ["age", "coin", "daughter", "bread", "freeze", "2016", "0",  "2", "horse", "island" ]

right = 0
q = 0
while q < 10:
    print questions[q] 
    ans = raw_input(" > ")
    list_ans = ans.split(" ")
    i=0
    
    
    while (i <= len(list_ans) -1):
        if  list_ans[i] == anskey[q]:
            right = right + 1
            i = len(list_ans) + 1
        else:
		i = i + 1
    q = q + 1

print """
======================
RESULTS
======================
"""

if right < 3:
    print "You probably have a low iq- perhaps you may have a 'artistic brain' rather than a 'logical brain'."
elif right == 3 or right == 4:
    print "You are a LOGICAL THINKER."
elif 5 <= right <= 7:
    print "You are INTELLIAGANT." 
else:
    print "You are a true GENIUS."
print "                     "
print "====================== "
raw_input("Hit enter to exit.")	