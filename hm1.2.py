def sqrt(a):
    x = 1
    while True:
        oldValue = x
        x = 1/2*(x**2 + a)/x
        i += 1
        if abs(x - oldValue) < 0.0001:
            break
    return x

def equation(a,b,c):
    if a == 0 and b != 0:
        x = -c/b
        print("%0.3f" %(x))
    elif a != 0 and b == 0:
        if c>0:
            print("")
        else:
            x = sqrt(-c)/a
            print("%0.3f" %(x))
    elif a == 0 and b == 0:
        print("")
    else:
        d = b**2-4*a*c
        if d<0:
            print("")
        elif d == 0:
            x = -b/(2*a)
            print("%0.3f" %(x))
        else:
            x1 = (-b-sqrt(d))/(2*a)
            x2 = (-b+sqrt(d))/(2*a)
            print("%0.3f %0.3f" %(x1,x2))

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

equation(a,b,c)
