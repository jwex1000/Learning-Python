#!/usr/bin/env python

#this on is like scripts with argv
def print_two(*args):
    #this unpacks the arguments like argv module does
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)
    
#this just takes on argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
#this one takes not argument
def print_none():
    print "I got nothin'."
    
    
print_two ("josh","Wexler")
print_two_again ("Joshua", "Wexler")
print_one ("first!")
print_none()
