calc_status = 'On' 

def func_add(input_x, input_y):
    return (input_x + input_y)

while calc_status == 'On':
    ui_x = int(input("Enter your first number:\n"))
    ui_y = int(input("Enter your second number:\n"))

    ui_sum = func_add(ui_x, ui_y)
    print(f"The sum of the two values {str(ui_x)} and {str(ui_y)} is: {str(ui_sum)}")

    calc_status = input("'On' or 'Off'?\n")
    
print("The calculator is now 'Off'")

    
