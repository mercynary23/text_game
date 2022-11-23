arr_nba = ['Kobe', 'DeRozan', 'Allen', 'Walker', 'Wade']

def ordered(to_print):
    #len() tells you the actual number of items in the arr; in this case 5
    #The returned value of '5' is then fed into the range()
    #range() takes '5' as input and returns a 0 indexed array with 5 int items [0, 1, 2, 3, 4]; this is an arr independent of what you fed as a param 
    #Your iterator 'i' then mmaps to each of these 0 indexed values in the arr 
          
    for i in range(len(to_print)):
        print(str(i+1) + ". " + str(to_print[i]))

    print("The loop is now finished")

ordered(arr_nba)



