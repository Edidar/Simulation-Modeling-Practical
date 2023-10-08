n = 5
Ri = [0.44,0.81,0.14,0.05,0.93]
Ri.sort()
s2=[] #i/n
s3 = [] #i/n-Ri
s4 = []  #Ri-(i-1)/n
for i in range(0,n,1):
    t2=(i+1)/n
    s2.append(t2)
    t3 = s2[i]-Ri[i]
    s3.append(t3)
    t4 = Ri[i]-(i-1+1)/n
    s4.append(t4)


dis  = {"Ri":Ri, "i/N" :s2, "i/N-Ri":s3 ,"Ri-(i-1)/N":s4}
import pandas as pd
r = pd.DataFrame(dis)
print(r)

D_p = max(s3)
D_N = max(s4)
print(D_p)
print(D_N)
if(D_p > D_N):
    t = D_p
else:
    t = D_N
    
if t<0.565:
     print('Accepted')
else:
    print("Rejected")
