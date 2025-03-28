import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You find yourself in a dark, eerie forest.")
    print_pause("The trees tower over you, whispering secrets in the wind.")
    print_pause("Ahead, you see a path that splits into two.")

def choose_path():
    print("Do you go left or right?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == 'left':
        dark_cave()
    elif choice == 'right':
        abandoned_cabin()
    else:
        print("Invalid choice! Try again.")
        choose_path()

def dark_cave():
    print_pause("You venture down the left path and find a dark cave.")
    print_pause("Inside, you hear the growl of a beast!")
    action = input("Do you 'fight' or 'run'? ").lower()
    if action == 'fight':
        print_pause("You bravely fight the beast and emerge victorious!")
        print_pause("You find a hidden treasure inside the cave!")
        print_pause("Congratulations, you win!")
    elif action == 'run':
        print_pause("You run back to the forest and safely escape.")
        choose_path()
    else:
        print("Invalid choice! Try again.")
        dark_cave()

def abandoned_cabin():
    print_pause("You take the right path and see an abandoned cabin.")
    print_pause("The door creaks as you step inside.")
    action = input("Do you 'explore' or 'leave'? ").lower()
    if action == 'explore':
        print_pause("You find a mysterious book that grants you magical powers!")
        print_pause("You become the master of the forest. You win!")
    elif action == 'leave':
        print_pause("You step outside and the cabin vanishes behind you.")
        choose_path()
    else:
        print("Invalid choice! Try again.")
        abandoned_cabin()

def start_game():
    intro()
    choose_path()
    print("Game over. Thanks for playing!")

start_game()
