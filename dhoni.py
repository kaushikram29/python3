a=int(input())
l=[]
x=n1//2+n1
for i in range(1,a+1):
    if i%2==0:
        l.append(i)
for i in range(1,a+1):
    if i%2!=0:
        l.append(i)
for i in range(1,a+1):
    if i%2==0:
        l.append(i)
print(x)
print(*l)
