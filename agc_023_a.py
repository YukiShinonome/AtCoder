N = int(input())
A = list(map(int, input().split()))
dic = {0:1}
sum_n = 0
count = 0


for a in A:
    sum_n += a
    if sum_n in dic:
        count += dic[sum_n]
        dic[sum_n] += 1
    else:
        dic[sum_n] = 1


print(count)