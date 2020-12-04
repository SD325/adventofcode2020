import re


CHECK = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: ("cm" in x and (150 <= int(x.replace("cm", "")) <= 193)) or
                     ("in" in x and (59 <= int(x.replace("in", "")) <= 76)),
    "hcl": lambda x: re.match(r"#[0-9a-f]{6}", x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric()
}


with open("inputs/day4.txt") as f:
    a = [x.replace('\n', ' ').strip() for x in f.read().split("\n\n")]
    p1 = p2 = 0
    for s in a:
        passport = {field.split(':')[0]: field.split(':')[1] for field in s.split()}
        p1 += all(key in passport for key in CHECK)
        p2 += all(key in passport and func(passport.get(key)) for key, func in CHECK.items())
    print(p1)
    print(p2)
