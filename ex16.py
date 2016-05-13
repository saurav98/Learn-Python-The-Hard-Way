from sys import argv
#importing argv module from sys

script, filename = argv
#If you are writing or appending (but not reading)
#then a new file will be created within that name.

 
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^c). "
print "If you do want that, hit RETURN."
#it will ask to confirm.

raw_input('?')

print "Opening the file..."
target = open(filename,'w')
#Here it will open file to write. If file is not there then it will create it.
#r = read      , r+ = read and write
#w = write     , w+ = wite and read
#a = append


print "truncating the file. Goodbye!"
target.truncate()
#truncating means deleting everything in the file

print "Now I am going to ask you three lines. "

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
#this is a methode or function to write.
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()
