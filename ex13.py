from sys import argv
script, first, second, third = argv
#while typing python ex13.py in powershell type 3 variables(names etc)

print "The script is called:" ,script
print "Your first variable is:",first
print "Your second variable is:", second
print "Your third variable is:",third

f = int(first)
s = int(second)
t = int(third)

product = f*s*t
sum = f+s+t
print "The script is called:" ,script
print "Your first variable is:",first
print "Your second variable is:", second
print "Your third variable is:",third
print "Product of all the varibles is: %s"%product
print "Sum of all the variables is: %d"%sum