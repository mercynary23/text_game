print("\n")
print("Welcome to Greed_Island :D! Are you ready to die?\n")

sprite_move = input("Where would you like to go?\n")
print(sprite_move)

if sprite_move == 'n' or sprite_move == 'N':
    print("You're travelling North!")
elif sprite_move == 'e' or sprite_move == 'E':
    print("You're travelling East!")
elif sprite_move == 's' or sprite_move == 'S':
    print("You're travelling South!")
elif sprite_move == 'w' or sprite_move == 'W':
    print("You're travelling West!")
else:
    print("You have entered an invalid action!")




