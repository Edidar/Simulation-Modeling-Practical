x = int(input())
y = int(input())

if x < y:
    tem = y
    y = x
    x = tem
else:
    tem =x
for i in range(y,x):
    if int(i) % 5== 2 or  int(i) % 5==3:
        print(int(i))
