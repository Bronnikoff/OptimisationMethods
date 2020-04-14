a2 = 4.5
a1 = 72
a0 = 3
b2 = 1.5
b1 = 144
b0 = 4
d = 16

e1 = 0.1
e2 = 0.8

u0 = 10000

def norm(x):
    return (x[0]**2 + x[1]**2)**(0.5)

def x(u):
    x1 = (-a1 - u*((a1 - b1)/b2 - 2*d)) / (2*a2 + 2*u*(1 + a2/b2))
    x2 = (a2*x1 + (a1 - b1)/2)/b2
    return [x1, x2]

def F(u):
    xu = x(u)
    return a2*xu[0]**2 + b2*xu[1]**2 + a1*xu[0] + b1*xu[1] + a0 + b0 + u*(xu[0] + xu[1] - d)



def minus(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1]]

def quit(x1, x2, F1, F2):
    if norm(minus(x1, x2)) < e1 and abs(F1 - F2) < e2:
        return True
    return False


xk = x(u0)
Fk = F(u0)
uk = u0
print("u =", uk)
print("x =", xk)
print("F(x) =", Fk)
for i in range(20):
    print()
    uk *= 10
    xk_1 = x(uk)
    Fk_1 = F(uk)
    print("u =", uk)
    print("x =", xk_1)
    print("|x1 - x0| =", norm(minus(xk, xk_1)))
    print("|F1 - F0| =", abs(Fk - Fk_1))
    print("F(x) =", Fk_1)
    if quit(xk, xk_1, Fk, Fk_1):
        print("Критерий останова выполнен!")
        break
    xk = xk_1
    Fk = Fk_1




