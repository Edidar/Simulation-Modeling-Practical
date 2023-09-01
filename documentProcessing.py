import random
import pandas as pd
n = int(input("Enter the Document Number :"))
st = []
wt = []
ft = []
cumT=[]
bt = []
nj = []
nd=[]
#print("Enter 1st starting time:")

st.insert(0,0)
#print("Enter 1st working  time:")
wt.insert(0,45)
ft.insert(0,st[0]+wt[0])
cumT.insert(0,ft[0])
bt.insert(0,0)
nj.append(random.randint(51,59))
nd.insert(0,0)
i =1;
for i in range (1,(n+1)):
    n =random.randint(0,1)
    bt.append(n)
    nd.append(int(i))
    l = random.randint(51,59)
    nj.append(l)
    workT=random.randint(5,45)
    wt.append(workT)
    if bt[int(i-1)]==1:
        
        st.append(ft[int(i-1)]+5)
        ft.append(st[int(i)]+wt[int(i)])
        cumT.append(wt[i])
    else:
        st.append(ft[int(i-1)])
        ft.append(st[int(i)]+wt[int(i)])
        cumT.append(st[int(i)]+wt[int(i)])
    

dic={"Doument Number ":nd,"Start Time ": st ,"Work Time ":wt, "Finish Time":ft,"Cummulative Time":cumT,"Break Flag":bt,"Number of job":nj}

show= pd.DataFrame(dic)
print(show)