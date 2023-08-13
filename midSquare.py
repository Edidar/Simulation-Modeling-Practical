seed = int(input("Enter initail seed :"))
#seed = 2135
#print(type(seed))
tem = seed
def random():
    global seed
    s = str(seed ** 2) # conver to string string 
    while len(s) != 8:
        s = "0" + s
    seed = int(s[2:6])
    return seed
while 1:
    chek = random()
    if tem==chek or chek ==0:
        break
    print(chek)

