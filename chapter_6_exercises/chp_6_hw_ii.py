arr_planets = ["Mercury", "Venus", "Earth"]

def middle_item(arr):
    arr_size = int(len(arr))
    arr_middle_term = int((arr_size + 1) / 2) 
    arr_middle_index = arr_middle_term - 1 

    return arr[arr_middle_index]

middle_planet = middle_item(arr_planets)

print("We have the following collection of planets:\n")
for planet in arr_planets:
    print(f"Planet {planet}")

print(f"The middle planet from this set is: {middle_planet}")


