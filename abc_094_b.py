N, M, X = map(int, input().split())
A = map(int, input().split())
n1 = 0
n2 = 0
for a in A:
    if a < X:
        n1 += 1
    else:
        n2 += 1
if n1 <= n2:
    print(n1)
else:
    print(n2)