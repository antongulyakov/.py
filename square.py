

def square(a, b, c):
    import math
    D= b**2 - 4 * a * c
    if D < 0:
        x1 = x2 = None
    elif D == 0:
        x1 = x2 = -b / (2 * a)
    else:
        x1 = -(b + math.sqrt(d)) / (2 * a)
        x2 = -(b - math.sqrt(d)) / (2 * a)
    print("x1=", x1, "x2=", x2)


a = input("a:")
b = input("b:")
b = input("c:")
square(a, b, c)
input()
