import random
s = []
for _ in range(0,100,1):
    t = str(random.random())
    t1 = float(t[0:4])
    s.append(t1)

ct1=ct2=ct3=ct4=ct5=ct6=ct7=ct8=ct9=ct10=0
for i in range(0,100,1):
    if s[i]>=0 and s[i]<=0.1:
         ct1 =ct1+1
    elif s[i]>=0.1 and s[i]<=0.2:
        ct2 =ct2+1
    elif s[i]>=0.2 and s[i]<=0.3:
        ct3 =ct3+1
    elif s[i]>=0.3 and s[i]<=0.4:
        ct4 =ct4+1
    elif  s[i]>=0.4 and s[i]<=0.5:
        ct5 =ct5+1
    elif  s[i]>=0.5 and s[i]<=0.6:
        ct6 =ct6+1
    elif s[i]>=0.6 and s[i]<=0.7:
        ct7 =ct7+1
    elif s[i]>=0.7 and s[i]<=0.8:
        ct8 =ct8+1
    elif s[i]>=0.8 and s[i]<=0.9:
        ct9 =ct9+1
    elif s[i]>=0.9 and s[i]<=1:
        ct10 =ct10+1
o = [ ]
o.append(ct1)
o.append(ct2)
o.append(ct3)
o.append(ct4)
o.append(ct5)
o.append(ct6)
o.append(ct7)
o.append(ct8)
o.append(ct9)
o.append(ct10)
print(o)
l =sum(o)
print(l)
E = [10]*10 #assign list with 10 time 10 value
print(E)
O_E = []
o_E_2 = []
for i in range(0,10,1):
    tem = o[i]-E[i]
    O_E.append(tem**2)
    tem1 = O_E[i]/E[i]
    o_E_2.append(tem1) 

check = sum(o_E_2)


# let c_val = 16.9
c_val = 16.9
if check <c_val:
    print("Accpted")
else:
    
    print("Rejected")

          
