#Write two functions
#Function_1 will host the main game cascade
#Function_2 will absorb user input concerning direction 

def play_game():
    print("Welcome to Greed Island - are you ready to Die? XD")
    #ui_name = input("What is your name, Hunter?\n")
    ui_name = user_name_prompt()
    ui_dir = input(f"Where next {ui_name}?\n")

    if ui_dir == 'N' or ui_dir == 'n':
        print(f"Beware of the North {ui_name}")
    elif ui_dir == 'E' or ui_dir == 'e':
        print("I hear talk of grassland trolls in the East...")
    elif ui_dir == 'S' or ui_dir == 's':
        print("The night is dark and full of terrors in the South")
    elif ui_dir == 'W' or ui_dir == 'w':
        print(f"Are you sure this is wise {ui_name}?")
    else:
        print("Are you afraid?")

def user_name_prompt():
    return input("What is your name, Hunter?\n")

play_game()
    