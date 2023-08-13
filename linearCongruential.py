x = int(input("Enter the value of initail Seed : "))
tem =x
a = int(input("Enter the value of a : "))
c = int(input("Enter the value of c : ")) 
m = int(input("Enter the value of m : "))
#
while 1:
    xi=(a*x+c)%m
    Ri = xi/m 
    x = xi
    if xi == tem or xi==0:
        break
    
    print(x)    
