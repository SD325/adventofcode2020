def game(end_turn):
    last_spoken = {x: i+1 for i, x in enumerate(a)}
    curr_num = 0 if a.count(a[-1]) == 1 else a[::-1][1:].index(a[-1]) + 1
    for t in range(len(a)+1, end_turn):
        next_num = t - last_spoken[curr_num] if curr_num in last_spoken else 0
        last_spoken[curr_num] = t
        curr_num = next_num
    return curr_num


with open("inputs/day15.txt") as f:
    a = [int(x) for x in f.readline().strip().split(",")]
    print(game(2020))
    print(game(30000000))
