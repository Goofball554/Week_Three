x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))
z = int(input("Please enter another number: "))

if x > y:
    if x > z:
        print(x, " is the greatest number.")

if y > x:
    if y > z:
        print(y, "is the greatest number.")

if z > x:
    if z > y:
        print(z, "is the greatest number.")

if x == y:
    if x > z:
        print(x, " and ", y, " are the greatest numbers.")

if x == z:
    if x > y:
        print(x, " and ", z, " are the greatest numbers.")

if z == y:
    if z > x:
        print(z, " and ", y, " are the greatest numbers.")

if z == y:
    if z == x:
        print("There is no greatest number.")