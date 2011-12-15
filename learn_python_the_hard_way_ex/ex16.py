#!/usr/bin/env python

from sys import argv

script, filename = argv

print "We're going to erase the %r" % filename
print "If you don't want that, hit CRTL-C ."
print "If you do want that, hit RETURN"

raw_input ("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

#extra credit with the using %
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#this was really tricky because you have to include the variables within the same ()

#original exercise
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
