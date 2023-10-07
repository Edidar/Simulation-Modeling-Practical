import pandas as pd
k1=0.008
k2=0.002
a=[100]
b=[50]
c=[0]
T= [0]
t = 0
delta =0.1
n=10
for i in range(0,11,1):
    at=a[i] + (k2*c[i]-k1*a[i]*b[i])*delta
    bt = b[i] + (k2*c[i]-k1*a[i]*b[i])*delta
    ct = c[i] + 2*(k1*a[i]*b[i]-k2*c[i])*delta
    t = t + delta
    T.append(t)
    a.append(at)
    b.append(bt)
    c.append(ct)

dis = {"Time":T,"A":a,"B":b,"C":c}
r = pd.DataFrame(dis)
print(r)
