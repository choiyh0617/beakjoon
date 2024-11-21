M=list(map(int,input().split()))
S=list(map(int,input().split()))
m=0
s=0
for i in range(4):
    m+=M[i]
    s+=s[i]
if m>=s:
    print(m)
else:
    print(s)


M=list(map(int,input().split()))
S=list(map(int,input().split()))
m=0
s=0
for i in range(4):
    m+=M[i]
    s+=S[i]
if m>=s:
    print(m)
else:
    print(s)