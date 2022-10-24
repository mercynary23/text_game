n = input("Please enter an integer value:\n")
int_n = int(n)
 
if int_n < 100:
    print("The condition is true!")
else:
    print("The condition is false")

m = input("Let's take this further; insert another integer value:\n")
int_m = int(m)

if int_m < 18:
    print("You're still a child; you can't get on this ride!")
elif int_m < 21:
    print("Although you're over 18 you are still not of the legal drinking age; no alcohol for you!")
else:
    print("Welcome!")


#Double conditionals 

a = 3 
b = 5

if a == 3 and b == 4:
    print("The hypotenuse is 5.")
if a == 3 or b == 4:
    print("The hypoteneuse might be 5.")



