import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
h=100
g=9.8
y=np.empty(10,dtype='int')
yy=np.empty(10,dtype='int')
vmax=np.sqrt(2*g*h)
tmax=np.sqrt(h*2/g)
x=np.linspace(0,tmax,10)
for i in range(0,10,1):
    y[i]=h-0.5*g*x[i]**2
    yy[i]=g*x[i]
    
plt.plot(x,y,label='Height vs Time')
plt.plot(x,yy,label="velocity vs Time")
plt.grid()
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Time vs Height')
plt.legend(loc="best",shadow=True)
plt.show()