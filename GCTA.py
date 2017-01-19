import random, time, sys, custom_func, statistics

# Game intro
print("\n\nHello!")
time.sleep(1)
print("Welcome to generic-crappy-text-adventure, or GCTA for short!")
time.sleep(1)
print("Please type in your adventurer's name. \n")

statistics.username = str(input("---> ")).lower()

print("\nAnd so our adventure begins! \n")
time.sleep(1)
print("You wake up in a tavern. Blah blah blah.")
time.sleep(1)
print("You think to yourself 'Let's go kill some rats for that sweet sweet EXP'")
time.sleep(1)
print("You walk outside the tavern and immediately come across your arch-enemy, El ratto! (Because why the fuck not)")
time.sleep(1)

# Action choices
while statistics.rat_fight != "done":
    # Input "done" to easily skip battle, to allow for quicker testing.
    statistics.rat_fight = input("What would you like to do? (Type 'help' if you don't know!) \n\n ---> ").lower()
    if statistics.rat_fight == "help":
        custom_func.help()
    elif statistics.rat_fight == "fight":
        custom_func.fight(statistics.ratboss_name, statistics.ratboss_health, statistics.ratboss_damage, statistics.rat_fight)
    elif statistics.rat_fight == "health":
        custom_func.health()
    elif statistics.rat_fight == "run":
        custom_func.run(statistics.ratboss_name)
    elif statistics.rat_fight == "change name":
        custom_func.change_name()
    else:
        print("That's not a valid action")

print("End of part one!")
print(statistics.hero_health)
