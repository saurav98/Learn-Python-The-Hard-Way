from sys import argv
#we are importing module argv
script, filename = argv

txt = open(filename)
#txt is a new variable. open() is a new command introduced now.
#It will open filename. 


  
print "Here's your file %r:"% filename
print txt.read()
#Dot here is an  piece of operetor it will 
#do the operation (which is on the right) to the left object
#It is also known as a dot operator
#here there is parenthesis even though there is nothing 
#to add but we have to write like this only
print txt.close()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
print txt_again.close()
