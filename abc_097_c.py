s_list = list(input())
k = int(input())
s_sort = sorted(s_list)
a_list = []
for s in s_sort:
    idx = s_list.index(s)
    for i in range(1, 6):
        a_list.append("".join(s_list[idx:idx+i]))
    s_list[idx] = "@"
a = list(set(a_list))
for i, s in enumerate(a):
    if "@" in s:
        a[i] = s.replace("@", s_sort[0])
a = sorted(a)
print(a[k - 1])