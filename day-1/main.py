# Part One
with open('input.txt', 'r') as file:
    print(sum(abs(int(a) - int(b)) for a, b in zip(*[sorted(list(l)) for l in list(zip(*[l[:-1].split('   ') for l in file.readlines()]))])))

# Part Two
from collections import Counter
with open('input.txt', 'r') as file:
    l, r = list(zip(*[l[:-1].split('   ') for l in file.readlines()]))
    freq = Counter(r)
    print(sum(int(n)*freq[n] for n in l))