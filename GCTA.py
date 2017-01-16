import random
import time
import sys

# Our hero's stats
hero_health = 25
hero_damage = 3

# Acions
def help():
    print("\n\n")
    print("|---------------------------------------------------------|")
    print("|                GCTA - Help guide                        |")
    print("|                                                         |")
    print("|  Commands:        What does it do:                      |")
    print("|                                                         |")
    print("|  - fight          Fight the closest enemy (if possible) |")
    print("|  - run            Run away from enemy                   |")
    print("|  - heatlh         Check hero's health                   |")
    print("|  - change name    Change your hero's name               |")
    print("|                                                         |")
    print("|  Good luck hero. You're gonna need it.                  |")
    print("|                                                         |")
    print("|---------------------------------------------------------|")
    print("\n\n")

def fight(enemy_name, enemy_health, enemy_damage, fight_status):
    global hero_health
    global rat_fight
    global ratboss_health
    while enemy_health > 0 and hero_health > 0:
        enemy_health = enemy_health - hero_damage
        print("You strike " + enemy_name + " for a total of " + str(hero_damage) + " damage")
        time.sleep(1)
        hero_health = hero_health - enemy_damage
        print(enemy_name + " Strikes " + username + " For a total of " + str(enemy_damage) + " damage")
        time.sleep(1)
    if enemy_health > 0:
        print("You died. The end.")
        sys.exit()
    else:
        rat_fight = "done"
        print(enemy_name + " Was defeated!")

def run(enemy_name):
    global hero_health
    global rat_fight
    avoid_chance = random.randint(1, 20)
    if avoid_chance > 19:
        print("You get away!")
        rat_fight = "done"
    else:
        hero_health = hero_health / 2
        print(enemy_name + " chases after you and catches you, landing a critical hit dealing HALF your health")

def health():
    print("\n Your hero has " + str(hero_health) + " Health.\n")

def change_name():
    global username
    print("\nChoose a new username!")
    Username_change = input("\n---> ")
    username = Username_change

# Game intro
print("\n\nHello!")
time.sleep(1)
print("Welcome to generic-crappy-text-adventure, or GCTA for short!")
time.sleep(1)
print("Please type in your adventurer's name. \n")

username = str(input("---> ")).lower()

print("\nAnd so our adventure begins! \n")
time.sleep(1)
print("You wake up in a tavern. Blah blah blah.")
time.sleep(1)
print("You think to yourself 'Let's go kill some rats for that sweet sweet EXP'")
time.sleep(1)
print("You walk outside the tavern and immediately come across your arch-enemy, El ratto! (Because why the fuck not)")
time.sleep(1)
# Rat boss' Stats
rat_fight = "incomplete"
ratboss_health = 10
ratboss_damage = 1
ratboss_name = "El ratto"

# Action choices
while rat_fight != "done":
    # Input "done" to easily skip battle, to allow for quicker testing.
    rat_fight = input("What would you like to do? (Type 'help' if you don't know!) \n\n ---> ").lower()
    if rat_fight == "help":
        help()
    elif rat_fight == "fight":
        fight(ratboss_name, ratboss_health, ratboss_damage, rat_fight)
    elif rat_fight == "health":
        health()
    elif rat_fight == "run":
        run(ratboss_name)
    elif rat_fight == "change name":
        change_name()
    else:
        print("That's not a valid action")

print("End of part one!")
print(hero_health)
