import itertools
 
n, k = map(int, input().split())
s = input()

s_list = list(s)
sort_s_list = sorted(s_list)
if n == k:
    print(''.join(sort_s_list))
elif k == 1:
    print(s)
else:
    count = 0
    for w in itertools.permutations(sort_s_list):
        for w1, w2 in zip(s_list, w):
            if w1 != w2:
                count += 1
                if count > k:
                    break
        if count <= k:
            print(''.join(w))
            break
        else:
            count = 0