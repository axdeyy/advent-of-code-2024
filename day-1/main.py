# Part One
print(sum(abs(int(a) - int(b)) for a, b in zip(*[sorted(list(l)) for l in list(zip(*[l[:-1].split('   ') for l in open('input.txt')]))])))

# Part Two
print(sum(int(n)*__import__("collections").Counter(list(zip(*[l[:-1].split('   ')for l in open('input.txt','r')]))[1])[n]for n in list(zip(*[l[:-1].split('   ')for l in open('input.txt','r')]))[0]))