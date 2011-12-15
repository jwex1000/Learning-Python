x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s are those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny ?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

# Extra Credit
print " "
print "Extra Credit"

#the variable x is a string with a format variable that pulls in the integer 10
x = "there are %d types of people." % 10

#defines the variable binary as "binary"
binary = "binary"

#defines the do_not variable as "don't'"
do_not = "don't"

#defines the y variable as a string with two format string varioables. Those pull in the variables binary and do_not
y = "Those who know %s are those who %s." % (binary, do_not)

#this prints both varioables x and y with their other vaiables pulled in
print x
print y

#this repeats the x variable inside a string where it will print the exact variable (no formating)
print "I said: %r." % x

#this repeats the y variable inside a string where it will print the variable formated as a string
print "I also said: '%s." %y

#defines two variables. the second has a format variable that will pull in whatever is next to it (which is nothing for now)
hilarious = False
joke_evaluation = "Isn't that joke so funny ?! %r"

#the variable joke evaluation now pulls in the variable hilarious where it has the %r
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#this prints a concatinated string of w and e
print w + e

#2. there are only 3 places where a string is put in another string. The other one is a boolean value
