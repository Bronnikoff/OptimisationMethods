# Made by Max Bronnikov
e = 0.01
x0 = [0.0, 0.0]
h0 = 0.5

a11 = 1
a12 = -1
a22 = 2
b1 = 6
b2 = 12

nsteps = 3

def f(x):
    return a11*x[0]*x[0] + a12*x[0]*x[1] + a22*x[1]*x[1] + b1*x[0] + b2*x[1]

def gradient(x):
    return [2*a11*x[0] + a12*x[1] + b1, 2*a22*x[1] + a12*x[0] + b2]

def norm(x):
    return (x[0]*x[0] + x[1]*x[1])**(0.5)

def next_step(x, hk, i):
    g = gradient(x)
    if i % 2:
        return [x[0], x[1] - hk*g[1]]
    return [x[0] - hk*g[0], x[1]] 

def check1(x1):
    grad = gradient(x1)
    for i in range(2):
        if grad[i] >= e:
            return False
    return True

def check2(x1, x2):
    if f(x2) < f(x1):
        return True
    return False

def find_h(x, i):
    if i % 2:
        return 1 / (2*a22)
    return 1 / (2*a11)


xk = list(x0)
h = h0
x = [x0]
for i in range(nsteps):
    print("x[" + str(i) + "] = ", xk)
    print("f(x[" + str(i) + "]) = ", f(xk))
    print("g(x[" + str(i) + "]) = ", gradient(xk))
    if check1(xk):
        print("First condition done on itteration", i, "with value", xk)
        raise ValueError

    xk1 = next_step(xk, h, i)

    while not check2(xk, xk1):
        print("Second condition not done with h =", h, " because f(" + str(xk1) + ") =", f(xk1), ">=", f(xk), "= f(" + str(xk) + ")")
        print("Make h = h / 2")
        h /= 2
        xk1 = next_step(xk, h, i)


    print("h[" + str(i) + "] = ", h)
    print()
    print("Step by x_" + str(i % 2), "coordinat")

    xk = list(xk1)
    x.append(list(xk))
    print()

    
print("All itterations done")
print()
print("xmin =", xk)
print("f(x) = ", f(xk))
