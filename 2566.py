arr=[]
for i in range(9):
    arr.append(list(map(int,input().split())))
s=arr[0][0]
for i in range(9):
    for j in range(9):
        if arr[i][j]>=s:
            s=arr[i][j]
print(s)

for i in range(9):
    for j in range(9):
        if arr[i][j] == s:
            print(i+1,j+1)
