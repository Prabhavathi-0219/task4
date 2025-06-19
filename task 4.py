def intro():
    print("\nWelcome to the Adventure Game!")
    print("You're a traveler who comes across a mysterious forest.")
    print("Do you want to ENTER the forest or WALK away?")
    choice = input("Type 'enter' or 'walk': ").lower()

    if choice == "enter":
        forest_path()
    elif choice == "walk":
        print("\nYou walk away safely, but miss out on a great adventure.")
        end_game("neutral")
    else:
        print("Invalid choice.")
        intro()

def forest_path():
    print("\nYou step into the forest. It's quiet... too quiet.")
    print("Suddenly, you see two paths: one leads to a dark cave, another to a sunny hill.")
    choice = input("Do you go to the 'cave' or the 'hill'? ").lower()

    if choice == "cave":
        dark_cave()
    elif choice == "hill":
        sunny_hill()
    else:
        print("Invalid choice.")
        forest_path()

def dark_cave():
    print("\nThe cave is cold and damp. You hear a growl in the darkness.")
    choice = input("Do you 'run' or 'investigate' the sound? ").lower()

    if choice == "run":
        print("\nYou escape the cave, but you're now lost in the forest.")
        end_game("neutral")
    elif choice == "investigate":
        print("\nA wild bear appears! You're no match for it.")
        end_game("bad")
    else:
        print("Invalid choice.")
        dark_cave()

def sunny_hill():
    print("\nYou climb the sunny hill and discover a hidden village.")
    choice = input("Do you 'explore' the village or 'talk' to a villager? ").lower()

    if choice == "explore":
        print("\nYou find a treasure hidden behind one of the houses!")
        end_game("good")
    elif choice == "talk":
        print("\nThe villager gives you a map to find even more treasure.")
        end_game("good")
    else:
        print("Invalid choice.")
        sunny_hill()

def end_game(outcome):
    if outcome == "good":
        print("\n🎉 Congratulations! You had a successful adventure!")
    elif outcome == "bad":
        print("\n💀 Oh no! That didn't end well.")
    elif outcome == "neutral":
        print("\n😐 The adventure was uneventful, but you're safe.")
    print("The End.")

# Start the game
intro()
