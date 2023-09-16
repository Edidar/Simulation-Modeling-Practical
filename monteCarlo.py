import matplotlib.pyplot as plt
import numpy as np
import random as rn
import math
def F(x):
   return math.sin(x*pi/b)

pi =math.acos(-1) # which is pi
#print(pi)

X = []
N =10 #number of item
i = 0
c = 1.00
a = 1
b = 30
while i<=b:
  X.append(i)
  i+= 0.001

Y = [F(x) for x in X ]
#rint(X,Y)
#print(Y)
X_random = [rn.random()*b for _ in range(N)] # means that these objects are used internally

Y_random = [rn.random()*c for _ in range(N)]
#print(X_random)
#print(Y_random)

probability = [1 if(F(X_random[i])>=Y_random[i]) else 0 for i in range(N)]



Accept = probability.count(1)
reject = probability.count(0)

total_point = Accept + reject



print('total accept ',Accept)
print('total reject ',reject)

print('Total point ', total_point)

print('Acceptance ratio :',Accept/N)

print('Rejection ratio :',reject/N)



plt.figure(figsize=(15, 3)) #This will modify/change the width and height of the plot.

plt.plot(X,Y,color='black')
plt.scatter(X_random,Y_random,c = probability,cmap='brg',s=30) #cmap stands for colormap
plt.plot([0,30],[0,0],color='black')

plt.plot([0,30],[1,1],color='red')#upper line 0 to 30 x=1 for star end y=1  end
plt.xticks([i for i in range(b+1)]) #Get or set the current tick locations and labels of the x-axis
for i in range(b+1):
  plt.plot([i,i],[0,1],color='black')

plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('Monte_Carlo_Simulation')
plt.scatter(X_random,Y_random,c =probability,cmap ='brg') #rainbow
plt.colorbar()
plt.show()





'''faults = [[i+1,0] for i in range(b)]

for i in range(N):
  faults[int(X_random[i])][1]+= probability[i]

print('[Day, Faults]')

count_undercurve = 0
for f in faults:
  count_undercurve += f[1]
  print(f)

print('Fault count ',count_undercurve)'''



#X_random = [i*pi for _ in range(N)]