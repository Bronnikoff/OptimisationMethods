# Made by Max Bronnikov
e = 0.01
x0 = [0.0, 0.0]

a11 = 1
a12 = -1
a22 = 2
b1 = 6
b2 = 12

nsteps = 1

def f(x):
    return a11*x[0]*x[0] + a12*x[0]*x[1] + a22*x[1]*x[1] + b1*x[0] + b2*x[1]

def gradient(x):
    return [2*a11*x[0] + a12*x[1] + b1, 2*a22*x[1] + a12*x[0] + b2]

def back_gesse(x):
    return [
        [2*a22 / (4*a22*a11 - a12*a12), -a12 / (4*a22*a11 - a12*a12)],
        [-a12 / (4*a22*a11 - a12*a12), 2*a11 / (4*a22*a11 - a12*a12)]
    ]

def gesse(x):
    return [
        [2*a11, a12],
        [a12, 2*a22]
    ]

def MxV(M, V):
    return [M[0][0]*V[0] + M[0][1]*V[1], M[1][0]*V[0] + M[1][1]*V[1]]

def norm(x):
    return (x[0]*x[0] + x[1]*x[1])**(0.5)

def next_step(x):
    g = gradient(x)
    G = back_gesse(x)
    v = MxV(G, g)
    return [x[0] - v[0], x[1] - v[1]]

def check1(x1):
    if norm(gradient(x1)) < e:
        return True
    return False

def check2(x1, x2):
    if f(x2) < f(x1):
        return True
    return False


xk = list(x0)
x = [x0]

for i in range(nsteps):
    print("x[" + str(i) + "] = ", xk)
    print("f(x[" + str(i) + "]) = ", f(xk))
    print("g(x[" + str(i) + "]) = ", gradient(xk))
    print("H(x[" + str(i) + "]) = ", gesse(xk))
    print("H^-1(x[" + str(i) + "]) = ", back_gesse(xk))
    if check1(xk):
        print("First condition done on itteration", i, "with value", xk)
        raise ValueError
    xk1 = next_step(xk)
    if not check2(xk, xk1):
        print("Second condition not done with values:", xk1, xk, "cos", f(xk1), ">=", f(xk))
        raise ValueError
    xk = list(xk1)
    x.append(list(xk))
    print()


print("All itterations done")
print()
print("xmin =", xk)
print("f(x) = ", f(xk))


