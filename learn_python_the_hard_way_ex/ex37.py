import random

def fly_pplanet_start():
    print """You wake up in your bed on your spaceship.
Your computer purrs awake and says 'good morning capt. %s
We are currently ciriciling over Plant Python... We are getting life readings.
Shall we initiate landing sequence""" %(user_name)
    
    land = raw_input ("> ")
    
    if "Yes" in land:
        land_scene ()
    else:
        print "Too bad, we are going to make you land anyway. Where is your sense of adventure"
        land_scene ()

#player lands a chooses a wepon. This creates their damge capabilites for fights
def land_scene ():
    print """You land on planet python and take a look around.
It is a very densly populated forest with very little light.
The computer reminds you to choose a wepon to take with you on your adventure.
You can choose one of the following:
    Broad Sword: 
    Damage 2-5, ability frostbite (3 turns, 4 damage)

    Ray Gun:
    Damage 3-6, ability big blast (4 turns, 3 damage)

    Pink Flamingo:
    Damage 1-3, ability nut ball (2 turns, 10 damage) """
    
    while True:
        wepon_choice = raw_input ("Type the name of the wepon you want > ")
        #I want to pass the minimum, maximum damage and the ability number of turns and ability damage to use later
        if wepon_choice == "Broad Sword":
            choose_path (2, 5, 3, 4)
            break
        elif wepon_choice == "Ray Gun":
            choose_path (3, 6, 4, 3)
            break
        elif wepon_choice == "Pink Flamingo":
            choose_path (1,3, 2, 10)
            break
        else:
            print "That is not a wepon. please type the name like you see above."

def choose_path(mindam, maxdam, aturns, adam):
    print """ You set off on your jounrey! WHOO!
You see a path ahead with a fork in it. Which way do you take, left or right?"""
    while True:
        path_choice = raw_input ("> ")
        if path_choice == "right":
            print """ As you walk down the path, you all of a sudden see the crazed Dr. Pangloss on his Giant Gurella!
Dr. Pangloss seems very mad. He wants to fight you!"""
            badhp = 20
            badmindam = 5
            badmaxdam = 10
            fight (mindam, maxdam, aturns, adam, badhp, badmindam, badmaxdam)
            break
        elif path_choice == "left":
            simon (mindam, maxdam, aturns, adam)
            break
        else:
            print "please choose a path right or left"

def fight (mindam, maxdam, aturns, adam, badhp, badmindam, badmaxdam):
    pturn = 0
    if playerhp > 0 and badhp > 0 and aturns >= pturn:
        
#    print """ As you walk down the path, you all of a sudden see the crazed Dr. Pangloss on his Giant Gurella!
#Dr. Pangloss seems very mad. He wants to fight you!"""
#    
##thought about putting in a retreat function, but that seems stupid.
#    #the stats for the bad guy
#    panglosshp = 20
#    panglossmindam = 5
#    panglossmaxdam = 10
#    player_turn = 0
#    #there are three counters that need to go on 1. pangloss hp, if it gets below 20 he dies and the player moves on, 2. Player hp, if that gets below 50, the player dies, 3. If the number of turns gets past the ability thing, the player can use it then goes back to normal fighting
#    while panglosshp <= 20 and player_turn <= aturns:
#    # need to create a loop for all of panglosses hp
#        print "You currently have %d HP. Pangloss has %d HP. Do you attack or defend?" % (playerhp, panglosshp)
#        pmove = raw_input ("attack or defend > ")
#        
#        if pmove == "attack":
#            player_damamge = random.randint (mindam, maxdam)
#            print "You do %d points of damage" % (player_damage)
#            panglosshp = panglosshp - player_damage
#            pangloss_damage = random.randint (panglossmindam, panglossmaxdam)
#            print "Pangloss counter strikes and does %d point of damage to you" % (pangloss_damage)
#            playerhp = 
#        if pmove == "defend":
#            
#        else:
#                print "not a valid move! please type attack or defend."
#        print "You can use your ability! Do you want to?"
#   

#need to do a for loop the number of tunrs untill you want to do your ability

#Start of the game
print """Welcome to Python Plant.
This is a scary game that is all text! WHOO!
Get ready to have some fun!"""

print "What is your name?"
user_name = raw_input ("> ")
# the player has 50 hit points overall
playerhp = 50
    
print "Welcome %s" % (user_name)
fly_pplanet_start ()


