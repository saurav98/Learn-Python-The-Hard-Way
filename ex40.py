class Song(object):

    def __init__(self, lyrics):
        print "^"*10
        self.lyrics = lyrics
           	
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line	
        print "%"
happy_bday = Song(["Happy birthday to you",
               "I don't want to get sued",
			   "So i'll stop right here"])

			   

			   
bulls_on_parde = Song(["They rally around the family",
                      "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parde.sing_me_a_song()		

print """
::::::::::::
"""


			  
class Song(object):

    def __init__(self, lyrics):
        print "^"*10
        self.lyrics = lyrics
           	
#    def sing_me_a_song(self):
        for line in self.lyrics:
            print line	
        print "%"*10
happy_bday = Song(["Happy birthday to you",
               "I don't want to get sued",
			   "So i'll stop right here"])

			   

			   
bulls_on_parde = Song(["They rally around the family",
                      "With pockets full of shells"])

#happy_bday.sing_me_a_song()

#bulls_on_parde.sing_me_a_song()		

print "::"*10
print

			  
			   			   