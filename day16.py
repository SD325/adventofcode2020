with open("inputs/day16.txt") as f:
    inp = [ll.strip() for ll in f.readlines()]
    fields, valid_ranges, tickets = [], [], []
    for l in inp:
        if 'or' in l:
            fields.append(l[:l.index(":")])
            l = l[l.index(":")+1:]
            t1 = l.split()[0].split('-')
            valid_ranges.append((int(t1[0]), int(t1[1])))
            t2 = l.split()[2].split('-')
            valid_ranges.append((int(t2[0]), int(t2[1])))
        elif 'ticket' in l or len(l) == 0:
            pass
        else:
            tickets.append([int(x) for x in l.split(',')])
    # Part 1
    print(sum(x if not any(a <= x <= b for a, b in valid_ranges) else 0 for t in tickets for x in t))

    # Part 2
    valid_tickets = [t for t in tickets if all(any(a <= x <= b for a, b in valid_ranges) for x in t)]
    field_ranges = {fields[i]: (valid_ranges[2*i], valid_ranges[2*i+1]) for i in range(len(valid_ranges)//2)}
    candidates = {fd: [] for fd in fields}
    for fd, (r1, r2) in field_ranges.items():
        (a, b), (c, d) = r1, r2
        for i in range(len(valid_tickets[1])):
            if all(a <= t[i] <= b or c <= t[i] <= d for t in valid_tickets[1:]):
                candidates[fd].append(i)

    finished = {}
    while not all(len(l) == 1 for l in candidates.values()):
        new_finished = {fd: l[0] for fd, l in candidates.items() if len(l) == 1 and fd not in finished}
        for fd, idx in new_finished.items():
            for fd2 in candidates:
                if fd != fd2 and idx in candidates[fd2]:
                    candidates[fd2].remove(idx)
        finished.update(new_finished)

    prod = 1
    for fd, i in finished.items():
        if fd.startswith('departure'):
            prod *= tickets[0][i]
    print(prod)
