print("Welcome to Greed Island :D! Are you ready to die?")

action_input = input("Where would you like to go?\n")
print(action_input)

if action_input == 'n':
    print("Go North!")
elif action_input == 'e':
    print("Go East!")
elif action_input == 'w':
    print("Go West!")
elif action_input == 's':
    print("Go South!")
else:
    print("Invalid action!")




