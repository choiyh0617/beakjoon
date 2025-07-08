import sys
input = sys.stdin.readline
a = int(input())
A = []
for _ in range(a):
    b, c = map(int, input().split())
    b %= 10
    if b == 0:
        A.append(10)
    else:
        B = []
        t = b
        while t not in B:
            B.append(t)
            t = (t * b) % 10
        i = (c - 1) % len(B)
        A.append(B[i])

for i in A:
    print(i)
