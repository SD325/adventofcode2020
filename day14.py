def p1():
    res = list(mask[::-1])
    rev_string = str(bin(value))[2:][::-1]
    for i, x in enumerate(rev_string):
        res[i] = x if mask[len(mask) - i - 1] == 'X' else mask[len(mask) - i - 1]
    res = ['0' if x == 'X' else x for x in res]
    mem[address] = int(''.join(res[::-1]), 2)


# Source: https://github.com/gfvirga/python_challenges/blob/master/Advent%20of%20Code%202020/day14.py
def p2():
    addr = f'{address:036b}'
    address_helper = [m if m == 'X' or m == a else '1' for a, m in zip(addr, mask)]
    orig = address_helper[:]
    for num in range(2 ** address_helper.count('X')):
        for char in bin(num)[2:].zfill(address_helper.count('X')):
            address_helper[address_helper.index('X')] = char
        mem2[''.join(address_helper)] = value
        address_helper = orig[:]


with open("inputs/day14.txt") as f:
    mem, mem2, mask = {}, {}, ''
    for line in f.readlines():
        if line[:3] == 'mem':
            address = int(line[line.index('[')+1:line.index(']')])
            value = int(line[line.index('=')+1:].strip())
            p1()
            p2()
        else:
            mask = line[line.index('=')+1:].strip()
    print(sum(mem.values()))
    print(sum(mem2.values()))
