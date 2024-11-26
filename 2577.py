L = [0,0,0,0,0,0,0,0,0,0]
a=int(input())
b=int(input())
c=int(input())

s = str(a*b*c)

for i in range(len(s)) :
    L[int(s[i])]+=1

for i in range(10):
    print(L[i])