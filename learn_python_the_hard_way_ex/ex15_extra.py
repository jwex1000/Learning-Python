#!/usr/bin/env python

# this imports the argv module from the sys libaray
print "What is the name of the file you are looking for?"
filename = raw_input("> ")

#creates a variable txt and opens the variable passed into it from the argv module
txt = open (filename)

#Shows the user what the file name is
print "Here's your file %r:" % filename
#shows the actualy contents of the file by performing the read method on the txt variable
print txt.read()
txt.close()
print txt.closed
#asks the user to retype the file name and will see it again
print "I'll also ask you to type it again:"
#put whatever the user writes into the file_again variable
file_again = raw_input("> ")

#puts the open file from the file_again variable into the txt_again variable
txt_again = open (file_again)

#shows the user the contents of the file
print txt_again.read()
txt_again.close()
