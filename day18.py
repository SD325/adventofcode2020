import re


class P1(int):
    def __add__(self, x):
        return P1(self.real + x.real)

    def __sub__(self, x):
        return P1(self.real * x.real)


class P2(int):
    def __add__(self, x):
        return P2(self.real * x.real)

    def __mul__(self, x):
        return P2(self.real + x.real)


with open("inputs/day18.txt") as f:
    inp = [ll.strip().replace('*', '-') for ll in f.readlines()]
    print(sum(eval(re.sub(r"(\d+)", r"P1(\1)", l)) for l in inp))
    print(sum(eval(re.sub(r"(\d+)", r"P2(\1)", l.replace('+', '*').replace('-', '+'))) for l in inp))
