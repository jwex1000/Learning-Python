#!/usr/bin/env python

def amazing(a, b, c):
    #add 100 to a
    d = a + 100
    print d + b + c

amazing (1, 3, 4)

print "lets give our function 3 numbers to add with 100"
num1 = int (raw_input ("give us your first number --> "))
num2 = int(raw_input ("give us your second number --> "))
num3 = int (raw_input ("give us your last number--> "))

amazing (num1, num2, num3)