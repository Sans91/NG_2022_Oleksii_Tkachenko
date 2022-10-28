import math


a = float(input("type number a\n>>"))
b = float(input("type number b\n>>"))
c = float(input("type number c\n>>"))

D = b * b - 4 * a * c
if D > 0:
    Droot = math.sqrt(D)
    x1 = (-b + Droot)/(2 * a)
    x2 = (-b - Droot)/(2 * a)
    print(f"x1 ={x1},\nx2 = {x2}")
elif D == 0:
    x = -b /  (2 * a)
    print(f"x = {x}")
else:
    print("there are no roots")