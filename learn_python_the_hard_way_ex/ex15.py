#!/usr/bin/env python

# this imports the argv module from the sys libaray
from sys import argv

#passess in whatever was writen as an argument in the terminal execution comand for the file
#then it puts that argument into the filename variable
script, filename = argv

#creates a variable txt and opens the variable passed into it from the argv module
txt = open (filename)

#Shows the user what the file name is
print "Here's your file %r:" % filename
#shows the actualy contents of the file by performing the read method on the txt variable
print txt.read()

#asks the user to retype the file name and will see it again
print "I'll also ask you to type it again:"
#put whatever the user writes into the file_again variable
file_again = raw_input("> ")

#puts the open file from the file_again variable into the txt_again variable
txt_again = open (file_again)

#shows the user the contents of the file
print txt_again.read()

