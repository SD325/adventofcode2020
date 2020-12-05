def binary(bsp, l, r):
    if l == r:
        return l
    if bsp[0] == 'F' or bsp[0] == 'L':
        return binary(bsp[1:], l, r - (r - l) // 2 - 1)
    else:
        return binary(bsp[1:], l + (r - l) // 2 + 1, r)


with open("inputs/day5.txt") as f:
    a = f.read().split()
    seat_ids = [binary(s[:7], 0, 127) * 8 + binary(s[7:], 0, 7) for s in a]
    p1 = max(seat_ids)
    print(p1)
    seat_ids = sorted(seat_ids)
    p2 = seat_ids[0]
    for st in seat_ids:
        if p2 != st:
            print(p2)
            break
        p2 += 1
