def p1(nums):
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            if nums[a] + nums[b] == 2020:
                return nums[a] * nums[b]


def p2(nums):
    for a in range(len(nums)):
        for b in range(a + 1, len(nums)):
            for c in range(b + 1, len(nums)):
                if nums[a] + nums[b] + nums[c] == 2020:
                    return nums[a] * nums[b] * nums[c]


with open("inputs/day1.txt") as f:
    arr = [int(line.strip()) for line in f]

print(p1(arr))
print(p2(arr))
