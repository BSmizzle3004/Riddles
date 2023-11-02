from inventory import create_inventory, add_gold, possible_items, random_item, display_inv, check_empty_inventory
from riddles import present_riddle
from puzzles import naughts_and_crosses_game, run_snake_game
import time
import random

def start():
    print("""Welcome traveler to this text-based adventure game. In this game, you must collect weapons, solve puzzles, and defeat
deadly opponents in order to progress to the next rooms and collect your rewards
I wish you luck on your journey.
You are in a dark room.
There is a door to your right and left.
Which one do you take?""")

    while True:
        choice = input("> ")
        if choice.lower().startswith("l"):
            print("You enter into a room full of traps")
            dead("one of the traps trigger and pierces your chest with an arrow from the wall")
            break
        elif choice.lower().startswith("r"):
            print("""You stumble around until finding an ancient door handle.
    Attempting to open it, you figure a key is required in order to first unlock it.""")
            start_room(display_inv)
            break
        else:
            print("Please enter a valid choice")


def bear_room():
    print("There is a bear here.")
    print("The bear has lots of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("You could eat the honey or taunt the bear")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice.lower().startswith("e"):
            dead("The bear looks at you then slaps your face off.")
        elif choice.lower().startswith("t") and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice.lower().startswith("t") and bear_moved:
            dead("The bear gets angry and chases you down.")
        elif choice.lower().startswith("l"):
            start()
        else:
            print("I've no idea what that means.")

def start_room(display_inv):
    print("""In one corner of the room lies a bunch of half-broken barrels.
In the other lies a spider-infested crevice, guarding something with a slight shine, a glimmer of sorts.
Do you choose the barrels or the spiders?""")
    
    while True:
        choice = input("> ")

        if choice.lower().startswith("b"):
            print("""You wander towards the barrels, crouching as you get close in order to inspect them.
        clutching at the contents of the barrel you retrieve a pouch containing 20 gold coins""")
            inventory_data = create_inventory()
            add_gold(inventory_data,20)
            display_inv(inventory_data)
            start_room()
            break


        elif choice.lower().startswith("s"):
            print("""You approach the mysterious shiny object with caution
        Slowly reaching out your hand before retrieving ...""")
            time.sleep(2)
            print("\n")
            sword1 = random_item("swords")
            print(sword1, """"; a sharp-edged sword that will prove to come in handy during combat.
        On the other side of the handle is a key like structure, which may be used to unlock the door
        Would you like to add this to your inventory ?
        BE WARNED: you can only carry a certain amount of items at a time""")
        
            while True:
                choice = input("> ")
                if choice.lower().startswith("y"):
                    inventory_data = create_inventory()
                    inventory_data["swords"].append(sword1)
                    display_inv(inventory_data)
                    skele_pirate_room(inventory_data)
                    break
                elif choice.lower().startswith("n"):
                    inventory_data = create_inventory()
                    display_inv(inventory_data)
                    skele_pirate_room(inventory_data)
                    break
                else:
                    print("Please enter a valid choice")
            
        
        else:
            print ("Please enter a valid choice")
        

def skele_pirate_fight(inventory_data):
    if check_empty_inventory(inventory_data):
        dead("Your inventory is empty. You have nothing to fight with and are killed by the skelepirates")
    else:
        display_inv(inventory_data)
        choice = input("> ")
        if choice in inventory_data["swords"]:
            if choice.lower() == "sword1":
                print("""You swing your blade with precision injuring 2 of the skeleton pirates and killing 3")
You must choose whether to kill the final 2 or reason with them in the hopes that")
they will join you on your quest""")
                while True:  # Start an infinite loop for valid input
                    choice = input("> ").lower()
                    
                    if choice.startswith("r"):
                        print("You begin to reason with them, but hear the faint sound of footsteps lurking behind you.")
                        dead("A pirate a few inches from death itself, pierces your back with his cutlass.")
                        break  # Exit the loop if the choice is valid
                    elif choice.startswith("k"):
                        print("""You charge at the remaining 2 pirates, piercing both with your sword.
Looting the skeleton pirate's bodies, you find a small bottle with an unknown liquid inside.
Would you like to add this to your inventory? (yes or no)""")
                        choice = input("> ").lower()

                        if choice.startswith("y"):
                            potion1 = random_item("potions")
                            inventory_data["potions"].append(potion1)
                            print(f"You have added {potion1} to your inventory.")
                            display_inv(inventory_data)
                            puzzle_room(inventory_data)
                        break  # Exit the loop if the choice is valid
                    else:
                        print("Invalid choice. Please choose 'kill' or 'reason'.") 

            if choice.lower() == "sword2":
                print("""You slay 2 of the skeleton pirates by piercing them in the chest using sword2
Then thowing your sword in a javelin type fashion you impale 2 more
This leaves one more begging for mercy, you approach him with unmatched confidence
You must either leave him alive or kill him (leave or kill)""")
                choice = input("> ")
                if choice.lower().startswith("l"):
                    print("""You steal a bottle containing some kind of liquid inside and a key before walking away")
Leaving him thanking you for mercy""")
                    potion1 = random_item("potions")
                    inventory_data["potions"].append(potion1)
                    display_inv(inventory_data)
                if choice.lower().startswith("k"):
                    print("""You slay the final skeleton pirate walking away with nothing but a key and")
a bottle containing some kind of liquid""")
                    potion1 = random_item("potions")
                    inventory_data["potions"].append(potion1)
                    inventory_data["keys"] = ["Chest Key"]
                    display_inv(inventory_data)
                    chest_room(inventory_data)

            if choice.lower() == "sword3":
                print("""You pull out yor sword trembling with fear
Charging towards the skeleton pirates you dive to avoid the multitude of attacks
One by one you swipe at their bodies killing every last one of them
You approach what appears to be the leader of the skeleton pirates
You must choose betweenone of two keys, one containing the engraving of a heart
The other, an engraving of some kind of chest
Do you choose the heart or the chest (Enter heart or chest)""")
                choice = input("> ")
                potion1 = random_item("potions")
                inventory_data["potions"].append(potion1)
                if choice.lower().startswith("h"):
                    inventory_data["keys"] = "Heart Key"
                    display_inv(inventory_data)
                if choice.lower().startswith("c"):
                    inventory_data["keys"] = "Chest Key"
                    display_inv(inventory_data)
                    chest_room(inventory_data)
        else:
            print("The item must be in your inventory, please enter a valid choice")
            skele_pirate_fight(inventory_data)



def skele_pirate_room(inventory_data):
    print("""You approach the door and insert the key
You grab the handle before beginning to edge the door open
All seems quiet, perhaps too quiet as you peak around the opening
In the side furthest from you, you notice a skeleton pirate, siting with a map
Cautiously you shift closer towards the skeleton. Step. Step. Cachunk
You appear to have stepped on a pressure plate, the walls slowly bein to rustle before...
\n
5 skeleton pirates brought to life stare you down infront of your very eyes
How do you plan to escape?""")
    skele_pirate_fight(inventory_data)



def puzzle_room(inventory_data):
    print("""You enter the room and are faced with 3 options.
3 different puzzles or games from which you must choose one to defeat 
in order to progress to the next room.
you must choose 1, 2 or 3 each providing a different challenge""")
    choice = input("> ")
    if choice.lower() == "1":
        print("In order to pass this room you must solve a riddle")
        if present_riddle():
            print("You are now able to progress to the next room and are granted 30 gold for answering correctly")
            add_gold(inventory_data,30)
        else:
            print("""You must now participate in a different challenge in order to progress to the next room
please select either 2 or 3""")
            choice = input("> ")
            if choice.lower() == "2":
                naughts_and_crosses_game()
            if choice.lower() == "3":
                run_snake_game()
                if run_snake_game():
                    print("Congratulations! You have defeated the Snake Game!")
                    bear_room()
                else:
                    print("""You have been defeated by the snake game")
You must now participate in a different challenge in order to progress to the next room
please select either 1 or 2""")

    if choice.lower() == "2":
        naughts_and_crosses_game()
    
    if choice.lower() == "3":
        run_snake_game()

def chest_room(inventory_data):
    print("""You scan the room searching for a potential reward
Then you observe a hidden chest peaking from behind the vines
This time more cautiously than the last you approach the chest
before inserting the key and begining to twist it
You struggle to open the lid but it doesnt budge, but then realise a riddle must be solved
In order to obtain the reward""")
    if present_riddle(): 
        print("You continue on your path 50 gold richer.")
        add_gold(inventory_data,50)
        puzzle_room(inventory_data)
    else:
        print("You continue on your path with no extra reward")
        puzzle_room()

def dead(why):
    print(why)
    play_again()

def play_again():
    print('Do you want to play again? (yes or no)')
    if input("> ").lower().startswith('y'):
        start()
    else:
        print('Bye for now')
        sys.exit()