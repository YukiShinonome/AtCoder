N, X = map(int, input().split())
m = []
for i in range(N):
    m.append(int(input()))
sum_m = sum(m)
x = X - sum_m
num = len(m) + x // min(m)
print(num)