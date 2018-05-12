X = int(input())
a_list = []
for s in range(1, 32):
    for i in range(2, 10):
        a = s ** i
        if a > 1000:
            break
        a_list.append(a)
a2 = sorted(list(set(a_list)), reverse=True)
for n in a2:
    if n <= X:
        print(n)
        break