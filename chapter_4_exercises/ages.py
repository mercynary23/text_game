user_age = input("How old are you Sailor?\n")
int_user_age = int(user_age)

if int_user_age < 13:
    print("You aren't even a teenager yet mi'lad! Back to school for you!")
elif int_user_age < 18:
    print("A few more years lad; you'll be on the waters soon enough")
elif int_user_age > 18 and int_user_age < 30:
    print("Well shiver me timbers sonny! Are you ready to die? Harr Harr Harr!")
else:
    print("You're too old; stay home, you've done enough")

print("Never fold")


