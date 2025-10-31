print(r''' 
             _                                     
            | |                                    
            | |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
            | __| '__/ _ \/ _` / __| | | | '__/ _ \
            | |_| | |  __/ (_| \__ \ |_| | | |  __/
             \__|_|  \___|\__,_|___/\__,_|_|  \___|
                                       
             ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
print("You are at cross road. where do you want to go?")
print("\t Type \"left\" or \"right\".\n")
left_or_right = input().lower()
if left_or_right == "right":
    print("You Fall into a hole. Game Over.")
elif left_or_right == "left":
    print("You've come to a lake. There is an island in the middle of the lack.")
    print("\t Type \"wait\" to wait for a boat. or Type \"swim\" to swim across.")
    wait_or_swim = input().lower()
    if wait_or_swim == "swim":
        print("Attacked by trout. Game Over.")
    elif wait_or_swim == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. \nOne red, one yellow and one blue. which color do you choose?")
        red_blue_yellow = input().lower()
        if red_blue_yellow == "red":
            print("Burned by fire. Game Over.")
        elif red_blue_yellow == "blue":
            print("Eaten by beasts. Game Over.")
        elif red_blue_yellow == "yellow":
            print("You Found the Treasure. You Win!")
        else:
            print("You Entered a door that doesn't exist. Game Over.")
    else:
        print("You chose a option that doesn't exist. Game Over.")
else:
    print("You chose wrong direction. Game Over.")