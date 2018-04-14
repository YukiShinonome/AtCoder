n = input()
a = sorted(int(x) for x in input().split())
max_a = a[-1]
print(max_a, min(a, key=lambda x: abs(max_a - x * 2)))