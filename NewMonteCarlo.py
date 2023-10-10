import matplotlib.pyplot as plt
import random
import numpy as np
import math
print("Enter the value of a, b & c: ")
a = int(input())
b = int(input())
c = int(input())
in_area = 0
total_points = 0
x_lst = []
y_lst = []
def f(x):
    return np.sin(x)
for x in range(1,101,1):
    x = random.uniform(a,b+1)
    y = random.uniform(0,c+1)
    total_points += 1
    if y <= f(x):
        in_area = in_area+1
        x_lst.append(x)
        y_lst.append(y)
print("Total points: ", total_points)
x = np.linspace(0.15,3,100)
t = f(x)
print("Number of point in range: ", in_area)
plt.plot(x,f(x))
plt.title('$Monte Carlo Graph$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.axhline(color = 'black')
plt.axvline(color = 'black')
plt.scatter(x_lst, y_lst)
plt.show()