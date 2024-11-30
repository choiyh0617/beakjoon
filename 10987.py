a=input()
s=0
A=['a','e','i','o','u']
for i in range(len(a)):
    if a[i] in A:
        s+=1
    else:
        pass
print(s)