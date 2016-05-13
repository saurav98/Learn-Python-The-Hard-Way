from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
#This funcion will display the file.
	
def rewind(f):
    f.seek(0)
# This is a built in function . 0 indicates 0 bytes . 
#Hence seek will takes us to the beginning.
	
def print_a_line(line_count, f):
    print line_count, f.readline()
# readline is a function that reads a line and stops next if next time it has
# called then it will read the next line. 

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) 

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line =+ 1
print_a_line(current_line, current_file)

# we can write the above command as follows
# current_line += 1
