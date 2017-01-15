import random

# Our hero's stats
hero_health = 25
hero_damage = 3

# Acions
def help():
    print("There are two basic actions right now. \nfight or run")
    print("To do either just type either 'fight' or 'run' when asked for an action")

def fight(enemy_name, enemy_health, enemy_damage, fight_status):
    global hero_health
    global ratboss_health
    global rat_fight
    while enemy_health > 0 and hero_health > 0:
        enemy_health = enemy_health - hero_damage
        print("You strike " + enemy_name + " for a total of " + str(hero_damage) + " damage")
        hero_health = hero_health - enemy_damage
        print(enemy_name + " Strikes " + username + " For a total of " + str(enemy_damage) + " damage")
    if enemy_health > 0:
        print("You died. The end.")
        #INSERT CODE TO ABORT PROGRAM here
    else:
        rat_fight = "done"
        print(enemy_name + " Was defeated!")

def run(enemy_name):
    global hero_health
    global rat_fight
    avoid_chance = random.randint(1, 20)
    if avoid_chance > 10:
        print("You get away!")
        rat_fight = "done"

    else:
        hero_health = hero_health / 2
        print(enemy_name + " chases after you and catches you, landing a critical hit dealing HALF your health")

# Game intro
print("Hello!")
print("Welcome to generic-crappy-text-adventure, or GCTA for short!")
print("Please type in your adventurer's name.")

username = str(input("---> ")).lower()

print("And so our adventure begins! \n \n")
print("You wake up in a tavern. Blah blah blah. \nYou think to yourself 'Let's go kill some rats for that sweet sweet EXP'")

print("You walk outside the tavern and immediately come across your arch-enemy, El ratto! (Because why the fuck not)")

# Rat boss' Stats
rat_fight = ""
ratboss_health = 10
ratboss_damage = 1
ratboss_name = "El ratto"

# Action choices
while rat_fight != "done":
    # Input "done" to easily skip battle, to allow for quicker testing.
    rat_fight = input("What would you like to do? \n ---> ").lower()
    if rat_fight == "help":
        help()
    elif rat_fight == "fight":
        fight(ratboss_name, ratboss_health, ratboss_damage, rat_fight)
    elif rat_fight == "run":
        run(ratboss_name)
    else:
        print("That's not a valid action")

print("End of part one!")
print(hero_health)
