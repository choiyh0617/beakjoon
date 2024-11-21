# a=int(input())
# for i in range(1,a+1):
#     print(" "*a-i + '*'*i)

a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + '*'*i,end="")
    print(i-1*'*')

a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + '*'*i,end="")
    print((i-1)*'*')
for i in range(a-1,-1,-1):
    print(' '*(a-i)+'*'*i,end="")
    print('*'*(i-1))