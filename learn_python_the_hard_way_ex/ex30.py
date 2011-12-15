#!/usr/bin/env python

people = 30
cars = 40
buses = 15

if cars > people or buses > people:
    print "We should take the cars"
    #this will print
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide"
    
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses"
    #this will print
else:
    print "We still can't decide."
    
if people > buses:
    print "Alright, lets just take the buses."
    #this will print
else:
    print "Fine, let's stay home then."
