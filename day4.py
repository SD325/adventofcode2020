def check1(s, colons):
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = set(s[c - 3:c] for c in colons)
    if 'cid' in fields:
        fields.remove('cid')
    return fields == req_fields


def p1(l):
    ans = 0
    for s in l:
        colons = [i for i, letter in enumerate(s) if letter == ":"]
        ans += check1(s, colons)
    return ans


def check2(s, colons):
    valid = True
    for c in colons:
        field = s[c - 3:c]
        try:
            if field == 'byr':
                valid = (1920 <= int(s[c:c + 4]) <= 2002)
            elif field == 'iyr':
                valid = (2010 <= int(s[c:c + 4]) <= 2020)
            elif field == 'eyr':
                valid = (2020 <= int(s[c:c + 4]) <= 2030)
            elif field == 'hgt':
                valid = False  # change
            elif field == 'hcl':
                valid = False  # change
            elif field == 'ecl':
                ecl_valid = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
                valid = (s[c:c + 3] in ecl_valid)
        except:
            valid = False
        else:
            valid = True
    return valid


def p2(l):
    ans = 0
    req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for s in l:
        colons = [i for i, letter in enumerate(s) if letter == ":"]
        ans += check2(s, colons)
    return ans


with open("inputs/day4.txt") as f:
    a = [x.replace('\n', ' ').strip() for x in f.read().split("\n\n")]
    print(p1(a))
