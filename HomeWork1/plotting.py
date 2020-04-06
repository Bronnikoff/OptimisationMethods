# Made by Yaroslav Poskryakov and Max Bronnikov

from pocoordinat_down import x as x_pocoord
from gradient_faster_down import x as x_faster_down
from gradient_constant_step import x as x_const
from gauss_zeidel import x as x_gauss_zeidel
from newton import x as x_newton
import matplotlib.pyplot as plt
import numpy as np

e = 0.01
x0 = [0.0, 0.0]

a11 = 1
a12 = -1
a22 = 2
b1 = 4
b2 = 8

nlines = 7

ymin = -18
ymax = 0

xmin = -4
xmax = 0.5

step = 0.00005

def f(x):
    return a11*x[0]*x[0] + a12*x[0]*x[1] + a22*x[1]*x[1] + b1*x[0] + b2*x[1]

def create_line(x1_l, x2_l, a, b, c):
    for x2 in np.arange(xmin, xmax, step):
        D = b(x2)**2 - 4*a(x2)*c(x2)
        if D >= 0:
            x2_l.extend([x2, x2])
            x1_l.extend([(-b(x2) + D**(0.5)) / (2*a(x2)), (-b(x2) + D**(0.5)) / (2*a(x2))])

def gen_lines(x1_l, x2_l):
    for i in range(nlines):
        a = lambda x2: a11
        b = lambda x2: a12*x2 + b1
        c = lambda x2: a22*x2**2 + 8*x2 - (ymin + i*(ymax - ymin)/(nlines - 1))
        create_line(x1_l, x2_l, a, b, c)
        


def main():
    # solution:
    x1_k = [-24/7]
    x2_k = [-20/7]

    x1_p = [i[0] for i in x_pocoord]
    x2_p = [i[1] for i in x_pocoord]

    x1_f = [i[0] for i in x_faster_down]
    x2_f = [i[1] for i in x_faster_down]

    x1_c = [i[0] for i in x_const]
    x2_c = [i[1] for i in x_const]

    x1_g = [i[0] for i in x_gauss_zeidel]
    x2_g = [i[1] for i in x_gauss_zeidel]

    x1_n = [i[0] for i in x_newton]
    x2_n = [i[1] for i in x_newton]

    x1_l = []
    x2_l = []

    gen_lines(x1_l, x2_l)

    plt.plot(x1_p, x2_p, color = "y", label='Покоординатный')
    plt.plot(x1_f, x2_f, '--', color = "g", label='Быстрый спуск')
    plt.plot(x1_c, x2_c, '-.', color = "b", label='Градиентный метод с постоянным шагом')
    plt.plot(x1_g, x2_g, ':', color = "r", label='Метод Гаусса-Зейделя')
    plt.plot(x1_n, x2_n, '--', color = "coral", label='Метод Ньютона')
    plt.plot(x1_k, x2_k, 'o', label='Классическое решение')
    plt.plot(x1_l, x2_l, ',', color = 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-3.5, 0.2)
    plt.title("Графическое отображение методов")


    plt.legend()
    plt.grid()
    plt.show()
    return 0


main()
