def avatar_func(first_name, last_name, age):
    print(f"Your name is {first_name} {last_name} and you are {age} years old")

def avatar_conditional_access(first_name, last_name, age):
    if age < 18:
        age_lapse = int(18 - age) 
        print(f"Hi {first_name}! Appears you're too young for this ride; we'll see you in {age_lapse} years :D")
    elif 18 < age and age < 30:
        print(f"Right this way {first_name}; we've been expecting you")
    else:
        print("Relax Mr {last_name}")


user_first_name = input("What is your first name?\n")
user_last_name = input("What is your last name?\n")
user_age = int(input("What is your age?\n"))

avatar_func(user_first_name, user_last_name, user_age)
avatar_conditional_access(user_first_name, user_last_name, user_age)

def say_hello(name):
    print("Hello, " + name)

say_hello("Una")
