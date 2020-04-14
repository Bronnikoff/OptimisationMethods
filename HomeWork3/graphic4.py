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

def level_line(x1, value):
    return value / 3.0 - 5.0*x1 / 3.0


x1 = list(np.linspace(-20, 80, 1000))

y1 = list(map(first_x2, x1))
y2 = list(map(second_x2, x1))
y3 = list(map(third_x2, x1))
ymin = list(map(infinum, x1))
ymax = list(map(supremum, x1))

level_line150 = list(map(lambda x: level_line(x, 150), x1))
level_line180 = list(map(lambda x: level_line(x, 180), x1))



fig, ax = plt.subplots()


ax.plot(x1, y1, color = 'r', linewidth = 2, label = "x1 + x2 = 50")
ax.plot(x1, y2, color = 'yellow', linewidth = 2, label = "8x1 - 7x2 = 0")
ax.plot(x1, y3, color = 'orange', linewidth = 2, label = "2x1 + 3x2 = 180")
ax.plot([-20, 80], [40, 40], color = 'k', linewidth = 1.7, label = "x2 = 40")
ax.plot([60, 60], [-100, 100], color = 'k', linewidth = 1.7, label = "x1 = 60")
ax.plot([10], [40], 'o')


ax.plot(x1, level_line150, '--', color = 'chocolate', linewidth = 1.5, label = "линия уровня 150")
ax.plot(x1, level_line180, '--', color = 'deeppink', linewidth = 1.5, label = "линия уровня 180")





ax.plot([-20, 80], [0, 0], color = 'b', linewidth = 3)
ax.plot([0, 0], [-20, 80], color = 'b', linewidth = 3)


#ax.fill_between(x1, ymax, y1,
#                where= (ymax > y1),
#                facecolor='yellow')

#ax.fill_between(x1, ymax, y2,
#                where= (ymax > y2),
#                facecolor='green')

fill_y = list(map(lambda x: max(x), zip(y1, y2)))

#ax.fill_between(x1, fill_y, ymax,
#                where= (fill_y < ymax),
#                facecolor='grey')

ax.fill_between(x1, fill_y, y3,
                where= (fill_y < y3),
                facecolor='springgreen')

ax.fill_between(x1, ymax, y3,
                where= (ymax > y3),
                facecolor='white')

ax.fill_between([-30, 0], [100, 100], [0, 0],
                facecolor='white')

ax.fill_between([-30, 80], [-100, -100], [0, 0],
                facecolor='white')

ax.fill_between([-30, 80], [100, 100], [40, 40],
                facecolor='white')

plt.xlabel('x1')
plt.ylabel('x2')

ax.set_title("Четвёртый график")
ax.set_xlim([-10, 70])
ax.set_ylim([-10, 70])
ax.grid()

fig.set_figwidth(17)    #  ширина и
fig.set_figheight(10)    #  высота "Figure"

plt.legend()
plt.show()
