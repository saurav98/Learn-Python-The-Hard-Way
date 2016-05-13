from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file, "w")

print "The input file is %d bytes long" % len(indata)
#len stands for length. It gives length of file in bytes.


print "Does the output file exist? %r" % exists(to_file)
#exist is the functn that we
# have imported from os.patch
#It will display the result in True or False
print "Ready, hit RETURN to continue, CTRL- C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

print "Your new file is %d bytes long." % len(to_file)

out_file.close()
in_file.close()





