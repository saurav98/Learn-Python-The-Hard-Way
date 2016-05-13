my_name = ' Saurav Kanchan '
my_age = 18 #not a lie 
my_height = 74 #inches
my_weight = 180#lbs
my_eyes = 'Black'
my_teeth = 'White'
my_hair = "Brown"

print "Let's talk about %s." % my_name
#%s , %r and %d areknown as formatters.
#they tell python to take the variable on the right and put it in to replace the %s with its value.
print "He's %d inches tall."% my_height
print "He's %d pounds heavy."%my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."%(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee."%my_teeth

#this line is tricky try to get it exactly right
print "If I add %d , %d ,and %d I %d."%(my_age,my_height,my_weight,my_age+my_height+my_weight)