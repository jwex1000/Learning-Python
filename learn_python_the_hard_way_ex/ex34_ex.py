from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    while True:
        try:
            next = int(raw_input("please enter a number> "))
            break
        except ValueError:
            print "Ooops that was not a number, please try again!"
        
    if next < 50:
        print "Nice, you're not greedy, you win!"
        exit (0)
    else:
        dead("You greedy bastard!")


def bear_room():
    '''this takes the user down the bear path'''
    print "There is a bear in here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear? If you need help: type \"help\""
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "help":
           bear_room_help()
        elif next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews you leg off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means"

def bear_room_help():
    while True:
        print "hi! welcome to help! here are the options you can do"
        print """
        "take honey" you will take the honey from the bear
        "taunt bear" you will taunt the bear
        Now, are you read to tell us what you want to do?
        """
        next = raw_input ("yes or no> ")
        if "yes" in next:
           bear_room()
        elif "no" in next:
            print "whats wrong? here is the help you need"
        else:
            print "I dont understand plese type yes or no"

def cthulu_room():
    print "Here you see the great evil Cthulu"
    print "He, it, whatever stares at you and you go insane."
    print "Do you fleee for you life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulu_room()
        

def dead(why):
    print why, "good job!"
    exit(0)
    
def start():
    print "you are in a dark room."
    print "there is a door to your right and left."
    print "Which one do you take?"
     
    #i = 0
    
    #while i <= 4:
    #    next = raw_input("> ")
    #    if next == "left":
    #        bear_room()
    #    elif next == "right":
    #        cthulu_room()
    #    else:
    #        print "I dont understand"
    #        i = i + 1
    #dead ('youre an idiot!')
    
    for i in range(5):
        next = raw_input("> ")
        if next == "left":
            bear_room()
        elif next == "right":
            cthulu_room()
        else:
            print "I dont understand"
    dead ('youre an idiot!')

start()
