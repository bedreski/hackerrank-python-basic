def find_difference(a, b):
    remove_from_a = set()
    remove_from_b = set()
    aux = set()
    diff = []

    remove_from_a = a.difference(b)
    remove_from_b = b.difference(a)
    
    aux = remove_from_a.union(remove_from_b)

    diff = list(aux)
    diff.sort()

    return diff

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
print(*find_difference(a, b), sep='\n')