# Part One
print(sum(abs(int(a) - int(b)) for a, b in zip(*[sorted(list(l)) for l in list(zip(*[l[:-1].split('   ') for l in open('input.txt', 'r')]))])))

# Part Two
from collections import Counter
l, r = list(zip(*[l[:-1].split('   ') for l in open('input.txt', 'r')]))
print(sum(int(n)*Counter(r)[n] for n in l))