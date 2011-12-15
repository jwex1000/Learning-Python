#!/usr/bin/env python
def add(a,b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

#puzzle for extra credit

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "extra credit"

result = (age + (height - (weight * (iq / 2))))
print result

#attempt to use the functions as formulas
print "where you are trying to get is 80"
num1 = multiply(5,2)
num2 = add(10, 4)
num3 = subtract(7 ,8)

final = multiply(num1, subtract(num2, add(num3, 7)))

print final
