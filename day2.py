with open("inputs/day2.txt") as f:
    p1 = 0
    p2 = 0
    for line in f:
        arr = line.strip().split()
        dash = arr[0].index("-")
        a, b, ch, pw = int(arr[0][:dash]), int(arr[0][dash+1:]), arr[1][0], arr[2]
        p1 += (a <= sum(p == ch for p in pw) <= b)
        p2 += ((pw[a-1] == ch) != (pw[b-1] == ch))

print(p1)
print(p2)
