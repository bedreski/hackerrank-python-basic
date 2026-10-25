def mutation(s, n, c):
    l = list(s)

    if 0 <= n < len(l):
        l[n] = c

    s = ''.join(l)
    return s

#main
s = input()
n = int(input())
c = input()
print(mutation(s, n, c))