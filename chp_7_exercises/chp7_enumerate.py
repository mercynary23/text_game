arr_greeks = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta'] 

for i, value in enumerate(arr_greeks, 1):
    print(f"In position {str(i)} we have: {value}")

print("The loop has run it's course")

for i, value in enumerate(arr_greeks, 1):
    if i % 3 == 0:
        print(f"The index value of {value} is a multiple of 3")

print("The loop has run it's course")


