# dictionary is a data stucture.(a complex way to say)
# list is list = ["something"]
# dictionary is dictionry = {"something" = "other"}

# ######################### # 

# creat a mapping of state to abbrevation.

states = {
"Oregon": "OR",
"Florida": "FL",
"California": "CA",
"New York" : "NY",
"Michigan": "MI"
}

# creat a basic set of states and some cities in them


cities = {
'CA' : 'San francisko',
'MI' : "Detroit",
"FL" : "Jacksonville"
}

#add some cities.
cities["NY" ] ="New York"; cities["OR"] = "Portland"


#print out some cities
print "="*10
print "NY State has :", cities["NY"]
print "OR State has :", cities["OR"]

#print some states
print "@"*10
print "Michigan's abbrevation is :", states["Michigan"]
print "Florida's abbrevation is :", states["Florida"]

#do it by using the state then cities dict
print "%"*10
print """    Michigan has %s 
Florida has %s """%(cities[states["Michigan"]], cities[states["Florida"]] )


#print every state abbrevation
print "========================"
for state, abbrev in states.items():
    print "%s is abbrevated as %s"%(state, abbrev)
	
# print every cities
print "_"*10
for  abbrev,city in cities.items():
    print "{0} has the city {1}".format(abbrev, city)
	
# now do both at same time
print "/"*20
for state, abbrev in states.items():
    print "%s state is abbrevated as %s and has city %s"%(
	state, abbrev, cities[abbrev])
	
print "$"*10
#safely get an abbrevation by state that might not be there
state = states.get("Texas",None)

if not state:
    print "Sorry no Texas."

# get a city with a default value 
city = cities.get("TX", "Does Not Exist")
print "The city for TX is: ", city	


























