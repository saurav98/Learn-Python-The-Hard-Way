print "Let me check your BMI."
  
age = raw_input('How old are you?')
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")
x = int(weight)
y = int(height)
z = 100*x/y
q = 100*z/y
print "Your BMI is : ",
print q

print "So, you're %r old, %r tall and %r heavy."%(age,height,weight)


