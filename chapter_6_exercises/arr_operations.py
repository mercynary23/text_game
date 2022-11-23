arr_nba = ['MJ', 'Magic', 'Bird', 'LBJ', 'Kobe'] 
print(arr_nba)
print(len(arr_nba))

arr_nba.append("Olajuwon")
print(arr_nba)
print(len(arr_nba))

iterator = 0 

while iterator < (len(arr_nba)):
    print(f"At position {str(iterator)} we have {arr_nba[iterator]}")
    iterator = iterator + 1 

print("The loop has stopped")




