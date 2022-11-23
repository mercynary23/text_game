arr_food = [] 
arr_iterator = 0 

while arr_iterator < 3:
    user_fave_food = input("What food do you like?\n")
    arr_food.append(user_fave_food)
    arr_iterator = arr_iterator + 1

for food in arr_food:
    print(f"You like to eat {food}")



