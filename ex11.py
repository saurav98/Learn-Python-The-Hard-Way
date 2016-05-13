print "How old are ?",
age = raw_input()
#raw_input is a sysytem command.it takes what user types and put here.
 

print "How tall are you (in cm )?",
height = int((raw_input()))
#bcz of comma ans will be showed in side

print "How much do you weight (in kg?)",
weight = int(raw_input())

print "So, you're %r year old, %r meter tall and %r kg heavy."% (
       age, height, weight)
#here above code is two line because there shouldn't be more than 
#8 lines in  python, it is bad format of python.


print "And Your BMI is."
x = 10000*weight/height
print x/height