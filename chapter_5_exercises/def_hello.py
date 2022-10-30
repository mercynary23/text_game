def say_hello():
    print("Hello New World!")

say_hello()

answer = input("Would you like another greeting?\n")

if answer == 'Y' or answer == 'y':
    say_hello()


user_name = input("What is your name, Sailor?\n")

def sailor_hello(name):
    print(f"Land ahoy {name}!")

sailor_hello(user_name)


