s,c=input().split()
s=int(s)
c=int(c)
q=''
w=2
if(s+c<=3):
    for i in range(0,s+c):
        if(i%2!=0):
            q=q+'0'
        else:
            q=q+'1'
else:    
    for i in range(0,s+c):
        if(i==w):
            q=q+'0'
            if(q==c):
                w=w+2
            else:
                w=w+3
        else:
            q=q+'1'
o=len(q)-1
if(int(q[o])==0):
    print('-1')
elif s==1 and c==2: print("011")
else:
    print(q)
