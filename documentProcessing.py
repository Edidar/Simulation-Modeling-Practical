import pandas as pd

st=[]
wt=[45,16,5,29,33,25,21]
ft =[]
cm=[]
bf=[]
nj=[]
s=c=0
n=7
noj=57
#nj.append(noj)
for i in range(0,n,1):
    st.append(s)
    s+=wt[i]
    c+=wt[i]
    
    nj.append(noj)
    if(c>=60):
        bf.append(1)
        ft.append(s)
        s+=5
        cm.append(c)
        c=0
    else:
        bf.append(0)
        ft.append(s)
        cm.append(c)
    noj-=1

print(nj,st,ft,bf,)
dis ={"Start Time":st,"Work Time":wt,"Finish Time":ft,"Cummulative Time":cm,"Break":bf,"Number of Job":nj}
r = pd.DataFrame(dis)
print(r)