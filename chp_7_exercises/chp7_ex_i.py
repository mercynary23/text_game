#Counters; ranges; enumerate 

def pretty_print_ordered(to_print):
    i = 1 
    for item in to_print:
        print(str(i) + "." + str(item))
        i = i + 1 

arr_test = ['Gold', 'Silver', 'Myrhh'] 

pretty_print_ordered(arr_test)

