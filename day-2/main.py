# Part One
print(sum(all(a + 1 <= b <= a + 3 for a, b in __import__("itertools").pairwise(int(x) for x in l.strip().split(' '))) or all(a - 3 <= b <= a - 1 for a, b in __import__("itertools").pairwise(int(x) for x in l.strip().split(' '))) for l in open('input.txt')))

# Part Two
print(sum(any(all(a + 1 <= b <= a + 3 for a, b in __import__("itertools").pairwise(int(x) for x in [x for idx, x in enumerate(l.strip().split(' ')) if idx != i])) or all(a - 3 <= b <= a - 1 for a, b in __import__("itertools").pairwise(int(x) for x in [x for idx, x in enumerate(l.strip().split(' ')) if idx != i])) for i in range(len(l) + 1)) for l in open('input.txt')))