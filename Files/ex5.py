
my_name   = "Nickolas A Kusman"
my_age    = 21
my_height = 67
my_weight = 180
my_eyes   = "Blue"
my_teeth  = "White"
my_hair   = "Brown"

print "Let's talk about %s." % my_name
print "He's %d inches tall," % my_height
print "When converted to feet, because he's not a heathen. makes him:" , my_height / 12 , "feet tall"
print "He's approximately %d pounds heavy." % my_weight
print "actually, that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, so make sure to get it right

print " If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight
)

#Note to self:
#%s appears to be for strings
#%r ?????????????????????
#%d appears to be for integers
#%f is for Floating point numbers
