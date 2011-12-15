#!/usr/bin/env python

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"
    #this will print
if people > cats:
    print "Not many cats! The world is saved"
    #this will not print
if people < dogs:
    print "The world is drooled on!"
    #this will not print
if people > dogs:
    print "The world is dry!"
    #This will print
    
dogs += 5

if people >= dogs:
    print "People are greater then or equal to dogs."
    #will print
if people <= dogs:
    print "People are less than or equal to dogs."
    #will print
if people == dogs:
    print "People are dogs."
    #will print