def sum_of_inputs(input_x, input_y):
    sum_of_values = (input_x + input_y)
    return sum_of_values 

ui_init_calc_status = input("Press Y/N to turn the calc ON or keep it OFF:\n")

if ui_init_calc_status == 'Y':
    print("The calculator is now ON")
    ui_current_calc_status = 'Y' 
    while ui_current_calc_status == "Y": 
        ui_var_x = int(input("Enter your first value:\n"))
        ui_var_y = int(input("Enter your second value:\n"))

        ui_sum_of_x_y = sum_of_inputs(ui_var_x, ui_var_y)
        print(f"The sum of {str(ui_var_x)} and {str(ui_var_y)} is:\n {str(ui_sum_of_x_y)}")

        ui_current_calc_status = input("Would you like to add together another pair of numbers?\n")
        if ui_current_calc_status == 'Y':
            continue
        else:
            print("Calculator is shutting down")
            ui_current_calc_status = 'N' 
else:    
    print("You never even turned the calculator on...")

        
