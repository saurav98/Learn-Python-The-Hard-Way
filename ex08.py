formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
#here python will give output like we have typed with single quotes bcz python is going to print string in most efficient way
print formatter % (True,False,False,True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.",
                   "That you could type up right.",
				   "But it didn't sing.",
				   "So I said goodnight."
				   )
