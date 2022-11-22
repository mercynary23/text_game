def say_hello():
    print("Hello New World")

say_hello()

answer = input("Would you like another greeting?\n")
if answer == 'Y' or answer == 'y':
    say_hello()
else:
    print("Strength and Honour")


