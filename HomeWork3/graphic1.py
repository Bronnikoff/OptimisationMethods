import matplotlib.pyplot as plt
import numpy as np

def infinum(x1):
    return 0.0

def supremum(x1):
    return 100.0

def first_x2(x1):
    return 50 - x1

def second_x2(x1):
    return 8.0 * x1 / 7.0

def third_x2(x1):
    return 60 - 2*x1 / 3



x1 = list(np.linspace(-20, 80, 1000))

y1 = list(map(first_x2, x1))
y2 = list(map(second_x2, x1))
y3 = list(map(third_x2, x1))
ymin = list(map(infinum, x1))
ymax = list(map(supremum, x1))


fig, ax = plt.subplots()


line = ax.plot(x1, y1, color = 'r', linewidth = 2, label = "x1 + x2 = 50")


ax.plot([-20, 80], [0, 0], color = 'b', linewidth = 3)
ax.plot([0, 0], [-20, 80], color = 'b', linewidth = 3)


ax.fill_between(x1, ymax, y1,
                where= (ymax > y1),
                facecolor='springgreen')

ax.fill_between([-30, 0], [100, 100], [0, 0],
                facecolor='white')

ax.fill_between([-30, 80], [-100, -100], [0, 0],
                facecolor='white')

plt.xlabel('x1')
plt.ylabel('x2')

ax.set_title("Первый график")
ax.set_xlim([-10, 70])
ax.set_ylim([-10, 70])
ax.grid()

fig.set_figwidth(17)    #  ширина и
fig.set_figheight(10)    #  высота "Figure"

plt.legend()
plt.show()
