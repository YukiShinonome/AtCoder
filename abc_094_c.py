from statistics import median


N = int(input())
X = list(map(int, input().split()))
medi_X = median(X)
sort_X = sorted(X)

for x in X:
    if x < medi_X:
        print(sort_X[int((N + 1) / 2)])
    else:
        print(sort_X[int(((N + 1) / 2) - 1)])