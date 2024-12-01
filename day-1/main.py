# Part One
with open('input.txt', 'r') as file:
    print(sum(abs(int(a) - int(b)) for a, b in zip(*[sorted(list(l)) for l in list(zip(*[l[:-1].split('   ') for l in file.readlines()]))])))

