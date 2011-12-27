import random

def dead ():
    print "You died! oh man! that sucks, you died... so sorry."
    print "do you want to play again?"
    while True:
        play_again = raw_input ("yes or no? > ").lower()
        
        if play_again == "yes":
            fly_pplanet_start()
        elif play_again == "no":
            print "That is too bad. Hope you enjoyed the game!"
            break
        else:
            print "I don't understand. Please type yes or no"

def fly_pplanet_start():
    print """\nYou wake up in your bed on your spaceship.
Your computer purrs awake and says 'good morning capt. %s
We are currently circling over Plant Python... We are getting life readings.
Shall we initiate landing sequence""" %(user_name)
    
    land = raw_input ("> ").lower()
    
    if "yes" in land:
        land_scene ()
    else:
        print "Too bad, we are going to make you land anyway. Where is your sense of adventure"
        land_scene ()

#player lands a chooses a weapon. This creates their damage capabilities for fights
def land_scene ():
    print """\nYou land on planet python and take a look around.
It is a very densely populated forest with very little light.
The computer reminds you to choose a weapon to take with you on your adventure.
\nYou can choose one of the following:
    Broad Sword: 
    Damage 2-5, ability frostbite (3 turns, 4 damage)

    Ray Gun:
    Damage 3-6, ability big blast (4 turns, 8 damage)

    Pink Flamingo:
    Damage 1-3, ability nut ball (2 turns, 10 damage) """
    
    while True:
        wepon_choice = raw_input ("\nType the name of the weapon you want > ").lower()
        #I want to pass the minimum, maximum damage and the ability number of turns and ability damage to use later
        if wepon_choice == "broad sword":
            choose_path (2, 5, 3, 4)
            break
        elif wepon_choice == "ray gun":
            choose_path (3, 6, 4, 8)
            break
        elif wepon_choice == "pink flamingo":
            choose_path (1, 3, 2, 10)
            break
        else:
            print "That is not a weapon. please type the name like you see above."

def choose_path(mindam, maxdam, aturns, adam):
    print """\nYou set off on your journey! WHOO!
You see a path ahead with a fork in it. Which way do you take, left or right?"""
    while True:
        path_choice = raw_input ("> ").lower()
        playerhp = 50
        pturn = 0
        if path_choice == "right":
            print """\nAs you walk down the path, you all of a sudden see the crazed Dr. Pan gloss on his Giant Guruella!
Dr. Pangloss seems very mad. He wants to fight you!"""
            badhp = 20
            badmindam = 5
            badmaxdam = 10
            fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
            break
        elif path_choice == "left":
            print """\nAs you walk down the path, all of a suden a crazy man comes running out at you!
It is Simple Simon! The great retarted wizard. Simple Simon doesn't look nice... or smart... and he wants to fight you!"""
            badhp = 40
            badmindam = 3
            badmaxdam = 10
            fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
            break
        else:
            print "please choose a path right or left"

def fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn):
    # the player has 50 hit points overall
    while playerhp > 0 and badhp > 0:
        print "You currently have %d HP. He has %d HP. Do you attack or defend?" % (playerhp, badhp)
        pmove = raw_input ("attack or defend > ")
        
        if pmove =="attack" and aturns > pturn:
            player_damage = random.randint (mindam, maxdam)
            print "You do %d points of damage \n" % (player_damage)
            badhp = badhp - player_damage
            bad_damage = random.randint (badmindam, badmaxdam)
            print "He counter strikes and does %d point of damage to you \n" % (bad_damage)
            playerhp = playerhp - bad_damage
            pturn = pturn + 1
                #may want to blow out the denfense thing more
        elif pmove == "defend" and aturns > pturn:
            print "You defend yourself."
            pturn = pturn + 1
        #player can user their special ability
        elif aturns == pturn:
            print "you can now use your specal ability!"
            pmove = raw_input ("use special abiliy, yes or no?> ")
            if pmove == "yes":
                player_damage = adam
                badhp = badhp - player_damage
                pturn = 0
                print "You use your abilty and do %d points of damage. NICE!" % (player_damage)
            elif pmove == "no":
                print "you dont use your ability."
                pturn = 0
            else:
                print "i dont understand. Please type yes or no."
        else:
            print "I don't understand. please type attack or defend."
    if playerhp <= 0:
        dead ()
    elif badhp <= 0 and python_king == 0:
        print "\nHe dies slowly and painfully. nice job!"
        pythonking(mindam, maxdam, aturns, adam)
    elif badhp <= 0 and python_king == 1:
        win()

def pythonking (mindam, maxdam, aturns, adam):
    #player HP and turns
    playerhp = 50
    pturn = 0
    #python king stats for battle
    badhp = 35
    badmindam = 3
    badmaxdam = 10
    global python_king
    python_king = 1
    print """\nYou continue to walk down the path and eventually get to a temple!
The temple has a huge python carved above the door.
All of a sudden a huge Python comes out!
\nIt is the PYTHON KING!\n
You must fight him or he will kill you!"""
    fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)

def win ():
    print "\nYou deal the final blow to the Python King. He staggers and falls."
    print "You have won the game! Congrats! You are amazing."
    print "\nWould you like to play again?"
    while True:
        play_again = raw_input ("yes or no? > ").lower()
        
        if play_again == "yes":
            fly_pplanet_start()
        elif play_again == "no":
            print "That is too bad. Hope you enjoyed the game!"
            break
        else:
            print "I don't understand. Please type yes or no"
    
#Start of the game
print """Welcome to Python Plant.
This is a scary game that is all text! WHOO!
Get ready to have some fun!"""

print "What is your name?"
user_name = raw_input ("> ")
    
print "\nWelcome %s" % (user_name)
python_king = 0
fly_pplanet_start ()



