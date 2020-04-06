# Made by Max Bronnikov
e = 0.01
x0 = [0.0, 0.0]

a11 = 1
a12 = -1
a22 = 2
b1 = 4
b2 = 8

nsteps = 3

def f(x):
    return a11*x[0]*x[0] + a12*x[0]*x[1] + a22*x[1]*x[1] + b1*x[0] + b2*x[1]

def gradient(x):
    return [2*a11*x[0] + a12*x[1] + b1, 2*a22*x[1] + a12*x[0] + b2]

def norm(x):
    return (x[0]*x[0] + x[1]*x[1])**(0.5)

def next_step(x, hk):
    g = gradient(x)
    return [x[0] - hk*g[0], x[1] - hk*g[1]]

def check1(x1):
    if norm(gradient(x1)) < e:
        return True
    return False

def check2(x1, x2):
    if f(x2) < f(x1):
        return True
    return False

def find_h(x):
    grad = gradient(x)
    return (grad[0]**2 + grad[1]**2) / (2*(a11*grad[0]**2 + a12*grad[0]*grad[1] + a22*grad[1]**2))


xk = list(x0)
x = [x0]
for i in range(nsteps):
    print("x[" + str(i) + "] = ", xk)
    print("f(x[" + str(i) + "]) = ", f(xk))
    print("g(x[" + str(i) + "]) = ", gradient(xk))
    hk = find_h(xk)
    print("h[" + str(i) + "] = ", hk)
    if check1(xk):
        print("First condition done on itteration", i, "with value", xk)
        raise ValueError
    xk1 = next_step(xk, hk)
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
