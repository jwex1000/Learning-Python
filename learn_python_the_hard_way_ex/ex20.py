#!/usr/bin/env python

#imports the argv module from the system
from sys import argv

script, input_file = argv

#defines our functions to be called
#print_all uses the read method for the argument that is pased in through f
def print_all(f):
    print f.read()
    
#rewind sets the value of where the program is to 0 in the text file
def rewind(f):
    f.seek(0)
    
#this reads the line number and then goes on to the next line
def print_a_line(line_count, f):
    print line_count, f.readline()
    
current_file = open(input_file)

print "First let's print the whole file: \n"

print_all (current_file)

print "Now let's rewind, kind of like a tape."
#this calls the rewind function so that the file will be read from the start
rewind(current_file)

print "Let's print three lines"

current_line = 1
print_a_line(current_line, current_file)
#current_line is equal to 1

current_line += current_line
print_a_line(current_line, current_file)
#current_line is equal to 2

current_line = current_line + 1
print_a_line(current_line, current_file)
#current_line is equal to 3

current_file.close()

x =1
x +=x
