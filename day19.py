def p1(n):
    if n in CHARS:
        return CHARS[n]
    all_messages = set()
    loop = []
    for t in RULES[n]:
        messages = ['']
        if n in t:
            loop.append(t)
            continue
        for u in t:
            messages = [m+l for m in messages for l in p1(u)]
        all_messages.update(messages)
    CHARS[n] = all_messages
    return all_messages


def p2(m, idx, loc):
    if idx in CHARS:
        return {loc + 1} if loc < len(m) and CHARS[idx] == m[loc] else set()
    valid_lens = set()
    for r in RULES[idx]:
        curr = {loc}
        for part in r:
            temp = set()
            for l in curr:
                temp |= p2(m, part, l)
            curr = temp
        valid_lens |= curr
    return valid_lens


with open("inputs/day19.txt") as f:
    inp = [ll.strip() for ll in f.readlines()]
    rules_list, messages_list = inp[:inp.index('')], inp[inp.index('')+1:]
    RULES = {int(r.split(": ")[0]): [tuple(int(t) for t in s.split()) for s in r.split(": ")[1].split(' | ')]
             for r in rules_list if '\"' not in r}
    CHARS = {int(r.split(": ")[0]): r.split(": ")[1].replace('\"', '') for r in rules_list if '\"' in r}
    orig_chars = {k: v[:] for k, v in CHARS.items()}
    # Part 1
    print(sum(m in p1(0) for m in messages_list))
    # Part 2
    RULES[8].append((42, 8))
    RULES[11].append((42, 11, 31))
    CHARS = {k: v[:] for k, v in orig_chars.items()}
    print(sum(len(m) in p2(m, 0, 0) for m in messages_list))
