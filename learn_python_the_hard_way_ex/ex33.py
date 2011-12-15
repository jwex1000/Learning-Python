
def while_loop (num_repeat):
    i = 0
    numbers = []
    while i < num_repeat:
        i = i + 1
        numbers.append(i)
    return numbers
    
print "show us a list of 6"
numbers = while_loop (6)
print numbers

def while_loop_good(num_repeat, incre):
    i = 0
    new_numbers = []
    while i < num_repeat:
        i = i + incre
        new_numbers.append(i)
    return new_numbers

print "How much do you want to count by?"
incre = int (raw_input ("> "))
print "How long would you like you list to be? "
num_repeat = int(raw_input ("> "))

new_numbers = while_loop_good(num_repeat, incre)

print "Then here is your new list: "
print new_numbers
    
print "the numbers: "

for num in numbers:
    print num

print "here is the same list of 6 but with a for loop"
new_list_for = []

for i in range (0, 7):
    new_list_for.append(i)
    
print new_list_for

new_numbers_for = []

print "here is the new list with a for loop"
for i in range (num_repeat, incre):
    new_numbers_for.append(i)
    
print new_numbers_for