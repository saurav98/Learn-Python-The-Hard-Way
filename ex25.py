#This is not a script that we was doing till now.
#It is a module. module will be called ex25 without a .py extension
#This is from python and not command line 


def break_words(stuff):
    """This function will break up words for us."""
    # Above line is a short explanation for the function.
	# It will appear when help is typed in python
    words = stuff.split(' ') 
	# .split is a built in function in python 
	#It will sepearate words with what we will type in ()
	#In our case we are splitting with blank space.
    return words

	
def sort_words(words):
    """Sorts the words. """
    return sorted(words)
	
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)	
    print word
	
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print word
	
def sort_sentences(sentence):
    """Takes in a  sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
	
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
	
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
	
#Here are the instruction to run this:

# 1 Start python by typing python in command line.
# 2 Save the file in script folder .
# 3 type import ex25   don't write .py
# 4 
# 5
# 6
