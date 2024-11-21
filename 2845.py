a,b=map(int,input().split())
c=list(map(int,input().split()))
A=[]
for i in range(5):
    A.append(c[i]-(a*b))
print(*A)