a=int(input())
l=[]
b=input()
b=b.split()
for i in set(b):
 if(b.count(i)>1):
  l.append(int(i))
if(len(l)>=1):
 print(l[0])
else:
 print("unique")
