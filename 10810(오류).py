# N,M=map(int,input().split())
# arr=[]
# for i in range(N):
#     arr.append(0)
# for i in range(M):
#     a,b,c=map(int,input().split())
#     arr[a:b]=c
# arr[2:5]=2
# print(arr)




#-------정답--------------
N,M=map(int,input().split())
arr=[]
for i in range(N):
    arr.append(0)
for i in range(M):
    a,b,c=map(int,input().split())
    for i in range(a-1,b):
        arr[i]=c
print(*arr)