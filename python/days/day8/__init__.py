from itertools import permutations

def part_2(data):
    mapper = {'acedgfb': '8', 'cdfbe': '5', 'gcdfa': '2', 'fbcad': '3',
    'dab': '7', 'cefabd': '9', 'cdfgeb': '6', 'eafb': '4', 'cagedb': '0', 'ab': '1'}
    mapper = {"".join(sorted(k)):v for k,v in mapper.items()}
    tot = 0
    for a,b in data:
        for p in permutations('abcdefg'):
            pmap = {a:b for a,b in zip(p, 'abcdefgh')}
            anew = [''.join(pmap[c] for c in x) for x in a]
            bnew = [''.join(pmap[c] for c in x) for x in b]
            if all(''.join(sorted(an)) in mapper for an in anew):
                bnew = [''.join(sorted(x)) for x in bnew]
                tot += int(''.join(str(mapper[x]) for x in bnew))
                break
    return tot

def solve():
    # split by | then by spaces
    data = [[s.split() for s in l.split('|')] for l in open('../input/day8', 'r')]

    # finds how many of 2nd part have length 2, 3, 4, 7
    part_1 = sum(len(list(filter(lambda x: len(x) in {2, 3, 4, 7}, y))) for _, y in data)


    return part_1, part_2(data)