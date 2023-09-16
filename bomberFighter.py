
import math
from matplotlib import pyplot as plt

#Boomber=[[80,0],[90,-2],[99,-5],[108,-9],[116,-15],[125,-18],[133,-23],[141,-29],[151,-28],[160,-25],[169,-21],[179,-20],[180,-17]]
XB=[80,90,99,108,116,125,133,141,151,160,169,179,180]
YB=[0,-2,-5,-9,-15,-18,-23,-29,-28,-25,-21,-20,-17]
XF=0.0
YF=50.0
XFL=[]
YFL=[]
XFL.append(XF)
YFL.append(YF)
VF=20
flag=0
temp=0
print("Path of Fighter.........")
print("X=",XF,"\t\t\t\tY=",YF)
for p,q in zip(XB,YB):
    distance=math.sqrt((p-XF)**2+(q-YF)**2)
    temp+=1
    print("Distance:",distance)
    if distance<=10:
        flag=1
        break
    else:
        sin=(q-YF)/distance
        cos=(p-XF)/distance
        XF+=VF*cos
        YF+=VF*sin
        XFL.append(XF)
        YFL.append(YF)
        print("X=",XF,"Y=",YF)

del XB[temp:13]
del YB[temp:13]
plt.title("Pure Pursuit Problem")
plt.xlabel("Boomber")
plt.ylabel("Fighter")
plt.plot(XB,YB,color='black',linestyle='dashed',linewidth=1,
         marker='o',markersize=10,markerfacecolor='green',
         markeredgecolor='blue')
        
plt.plot(XFL,YFL,color='green',linestyle='dashed',linewidth=1,
         marker='o',markersize=10,markerfacecolor='red',
         markeredgecolor='black')

plt.grid()
plt.show()
if flag==1:
    print("Fighter Attack the Boomber.")
else:
    print("Fighter Failed to Attack the Boomber.")