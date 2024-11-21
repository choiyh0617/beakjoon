arr=input()
c=[0]*26
for i in arr:
    c[ord(i)-97]+=1
print(*c)