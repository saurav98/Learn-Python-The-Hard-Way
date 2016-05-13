
import random 
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class %%%(%%%):":
"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self, ***)" :
"class %%% has-a __init__ that takes self and *** parameters.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function named *** that takes self and @@@ parameters.",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** function, and call it with parameters self, @@@.",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."
} #making dictionary named phrases.

 # do they want to drill phrases first
PHRASE_FIRST = False #set PHRASE_FIRST variable as false.
if len(sys.argv) == 2 and sys.argv[1] == "english": #sys.argv count the number of arguments.
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip()) #filling one by one words into list WORDS created above.


def convert(snippet, phrase): #snippet (:  a small piece of information or news) 
    class_names = [w.capitalize() for w in  # .capitalize will captilaze only the first letter in string  or word see upper function to do more cool stuff 
    random.sample(WORDS, snippet.count("%%%"))] #snippet.count("%%%") will count how much times the %%% has appeared in snippet. 
    other_names = random.sample(WORDS, snippet.count("***")) #it picks snippet.count("***") number of elements from WORDS and assigns it to other_names 
    results = [] #creting a blank list results
    param_names = []#creting a blank list param_names.

    for i in range(0, snippet.count("@@@")): 
        param_count = random.randint(1,3) # this function will set any value from 1 to 3 to param_count variable.
        param_names.append(', '.join(random.sample(WORDS, param_count))) # it will put a single element in param_names list.single element will be  of "sddf, dfsf, dfdf"

    for sentence in snippet, phrase:
        result = sentence[:]
        
 # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
# fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
# fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        results.append(result)
    return results

# keep going until they hit CTRL- D
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
				question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
