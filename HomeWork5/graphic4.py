import matplotlib.pyplot as plt
import numpy as np

def infinum(x1):
    return 0.0

def supremum(x1):
    return 100.0

def first_x2(x1):
    return 20 - x1*2.5

def second_x2(x1):
    return 12 - 0.5 * x1

def third_x2(x1):
    return 20 - 5*x1/3

def level_line(x1, value):
    return value / 6 - 5*x1/3


x1 = list(np.linspace(-20, 80, 1000))

y1 = list(map(first_x2, x1))
y2 = list(map(second_x2, x1))
y3 = list(map(third_x2, x1))
ymin = list(map(infinum, x1))
ymax = list(map(supremum, x1))

level_line150 = list(map(lambda x: level_line(x, 120), x1))
level_line180 = list(map(lambda x: level_line(x, 150), x1))



fig, ax = plt.subplots()


ax.plot(x1, y1, color = 'r', linewidth = 2, label = "5x1 + 2x2 = 40")
ax.plot(x1, y2, color = 'yellow', linewidth = 2, label = "x1 + 2x2 = 24")
ax.plot(x1, y3, color = 'orange', linewidth = 2, label = "10x1 + 6x2 = 120")
ax.plot([48 / 7], [60 / 7], 'o', label = "Решение")


ax.plot(x1, level_line150, '--', color = 'deeppink', linewidth = 1.5, label = "линия уровня 120")
ax.plot(x1, level_line180, '--', color = 'chocolate', linewidth = 1.5, label = "линия уровня 150")



ax.plot([-20, 80], [0, 0], color = 'black', linewidth = 2)
ax.plot([0, 0], [-20, 80], color = 'black', linewidth = 2)


#ax.fill_between(x1, ymax, y1,
#                where= (ymax > y1),
#                facecolor='yellow')

#ax.fill_between(x1, ymax, y2,
#                where= (ymax > y2),
#                facecolor='green')


#ax.fill_between(x1, fill_y, ymax,
#                where= (fill_y < ymax),
#                facecolor='grey')

ax.fill_between(x1, y1, ymax,
                where= (y1 < ymax),
                facecolor='springgreen')

ax.fill_between(x1, ymax, y2,
                where= (ymax > y2),
                facecolor='springgreen')

ax.fill_between(x1, ymin, y2,
                where= (ymin < y2),
                facecolor='white')

ax.fill_between(x1, ymin, y3,
                where= (ymin < y3),
                facecolor='white')

ax.fill_between([-30, 0], [100, 100], [0, 0],
                facecolor='white')

ax.fill_between([-30, 80], [-100, -100], [0, 0],
                facecolor='white')

ax.fill_between([-30, 80], [100, 100], [40, 40],
                facecolor='white')

plt.xlabel('x1')
plt.ylabel('x2')

ax.set_title("Область допустимых значений и оптимальное значение математической модели")
ax.set_xlim([-10, 30])
ax.set_ylim([-10, 40])
ax.grid()

fig.set_figwidth(17)    #  ширина и
fig.set_figheight(10)    #  высота "Figure"

plt.legend()
plt.show()
