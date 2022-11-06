#getting input from user on quadratic equation (ax^2 + bx + c = 0)
a = float(input("type number a\n>>"))
b = float(input("type number b\n>>"))
c = float(input("type number c\n>>"))

#finding discriminant by its formula
D = b * b - 4 * a * c
#if Discriminant is greater than 0, we need to find two variants of x with formula which has Discriminant root
if D > 0:
    #finding root
    Droot = pow(D, 1/2)
    x1 = (-b + Droot)/(2 * a)
    x2 = (-b - Droot)/(2 * a)
    print(f"x1 = {x1},\nx2 = {x2}")
#if Discriminant is 0, then there are only one x, which doesn't need root
elif D == 0:
    x = -b /  (2 * a)
    print(f"x = {x}")
#if Discriminant is lower than 0, then its doesn't have root, so it doesn't have solutions
else:
    print("there are no roots,\ntherefore no x to be found")