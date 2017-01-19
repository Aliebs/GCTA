import statistics, time, random

def help():
    print("\n\n")
    print("""
|---------------------------------------------------------|
|                GCTA - Help guide                        |
|                                                         |
|  Commands:        What does it do:                      |
|                                                         |
|  - fight          Fight the closest enemy (if possible) |
|  - run            Run away from enemy                   |
|  - heatlh         Check hero's health                   |
|  - change name    Change your hero's name               |
|                                                         |
|  Good luck hero. You're gonna need it.                  |
|                                                         |
|---------------------------------------------------------|
""")
    print("\n\n")



def fight(enemy_name, enemy_health, enemy_damage, fight_status):
    global hero_health
    global rat_fight
    global ratboss_health
    while enemy_health > 0 and statistics.hero_health > 0:
        enemy_health = enemy_health - statistics.hero_damage
        print("You strike " + enemy_name + " for a total of " + str(statistics.hero_damage) + " damage")
        time.sleep(1)
        statistics.hero_health = statistics.hero_health - enemy_damage
        print(enemy_name + " Strikes " + statistics.username + " For a total of " + str(enemy_damage) + " damage")
        time.sleep(1)
    if enemy_health > 0:
        print("You died. The end.")
        sys.exit()
    else:
        statistics.rat_fight = "done"
        print(enemy_name + " Was defeated!")

def run(enemy_name):
    global hero_health
    global rat_fight
    avoid_chance = random.randint(1, 20)
    if avoid_chance > 10:
        print("You get away!")
        statistics.rat_fight = "done"
    else:
        statistics.hero_health = statistics.hero_health / 2
        print(enemy_name + " chases after you and catches you, landing a critical hit dealing HALF your health")

def health():
    print("\n Your hero has " + str(statistics.hero_health) + " Health.\n")

def change_name():
    global username
    print("\nChoose a new username!")
    Username_change = input("\n---> ")
    username = Username_change
