arr_fave_food = [] 
more_items = True 

while more_items:
    user_input = input("What is your fave food?\n")
    #Triggered by pressing 'Enter'
    if user_input == "":
        more_items = False
    else:
        arr_fave_food.append(user_input)

print("This is a collection of your fave food:\n")

for food in arr_fave_food:
    print(f"{food}")


