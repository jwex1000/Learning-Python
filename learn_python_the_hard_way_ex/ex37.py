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
            choose_path (1, 3, 2, 10)
            break
        else:
            print "That is not a wepon. please type the name like you see above."

def choose_path(mindam, maxdam, aturns, adam):
    print """ You set off on your jounrey! WHOO!
You see a path ahead with a fork in it. Which way do you take, left or right?"""
    while True:
        path_choice = raw_input ("> ")
        playerhp = 50
        pturn = 0
        if path_choice == "right":
            print """ As you walk down the path, you all of a sudden see the crazed Dr. Pangloss on his Giant Gurella!
Dr. Pangloss seems very mad. He wants to fight you!"""
            badhp = 20
            badmindam = 5
            badmaxdam = 10
            fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
            break
        elif path_choice == "left":
            simon (mindam, maxdam, aturns, adam)
            break
        else:
            print "please choose a path right or left"

def fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn):
    # the player has 50 hit points overall
    while True:
        if playerhp > 0 and badhp > 0 and aturns > pturn:
            print "You currently have %d HP. Pangloss has %d HP. Do you attack or defend?" % (playerhp, badhp)
            pmove = raw_input ("attack or defend > ")
            
            if pmove == "attack":
                player_damage = random.randint (mindam, maxdam)
                print "You do %d points of damage \n" % (player_damage)
                badhp = badhp - player_damage
                bad_damage = random.randint (badmindam, badmaxdam)
                print "He counter strikes and does %d point of damage to you \n" % (bad_damage)
                playerhp = playerhp - bad_damage
                pturn = pturn + 1
                #fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
                #may want to blow out the denfense thing more
            elif pmove == "defend":
                print "You defend yourself."
                pturn = pturn + 1
                #fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
            #fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
        #player can user their special ability
        elif playerhp > 0 and badhp > 0 and aturns == pturn:
            print "you can now use your specal ability!"
            pmove = raw_input ("use special abiliy, yes or no?> ")
            if pmove == "yes":
                player_damage = adam
                badhp = badhp - player_damage
                pturn = 0
                print "You use your abilty and do %d points of damage. NICE!" % (player_damage)
                #fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
            elif pmove == "no":
                print "you dont use your ability."
                pturn = 0
                #fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
            #fight_one (mindam, maxdam, aturns, adam, playerhp, badhp, badmindam, badmaxdam, pturn)
        elif playerhp == 0:
            print "sorry, you died! \n \n"
            fly_pplanet_start()
        elif badhp == 0:
            print "He dies slowly and painfully. nice job!"
            pythonking(mindam, maxdam, aturns, adam, badhp, badmindam, badmaxdam, pturn)
        else:
            print "i dont understand"
        

def pythonking (mindam, maxdam, aturns, adam, badhp, badmindam, badmaxdam, pturn):
    print "you did it! you made it to the python king"
    
#Start of the game
print """Welcome to Python Plant.
This is a scary game that is all text! WHOO!
Get ready to have some fun!"""

print "What is your name?"
user_name = raw_input ("> ")
    
print "Welcome %s" % (user_name)
fly_pplanet_start ()


