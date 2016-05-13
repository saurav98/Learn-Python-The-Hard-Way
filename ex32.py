the_count = [1, 2, 3, 4, 5]
fruits = ["apples", 'oranges' , 'pears' , 'apricots']
change = [1, "pennies", 2, 'dimes' , 3 , 'quarters']
#in python the this is called lists.
#in other languges it is called arrays.

#this kind of for loops goes to a list.
for number in the_count:
    print "This is the count %d "% number
	
#same as the above 
for fruit in fruits:
    print 'A fruit of the type: %s ' % fruit 
	
#also we can go through mixed lists too 
#notice we have to use %r since we don't know what's in it 
for i in change:
    print ' I got %r ' % i

#we can also build lists, first start with an empty one
elements = []

#Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ' Adding %d to the list.'% i
    elements.append(i)
#above code can be written as: for i in range(6)
#because 0 is in  default   
	  #append is the function that lists understand
	  
	  
	  
#now we can print them out too
for i in elements:
    print "Elements was : %d " % i


print 'Now let us fill kanchan.'
	
kanchan = []

x = int(raw_input('starting from > '))
z = int(raw_input('till > '))
y = z +1
	
for i in range(x, y):
    print ' Adding %d to the list.'% i
    kanchan.append(i)
	
for i in kanchan:
    print "Kanchan has %r books." %i
	
print "But he does not read it."

saurav = [1, 2, 3]

saurav = range(5,10)

for i in saurav:
    print i

