from aoc import AdventOfCode as aoc
a = aoc(debug=True)

# Part 1
horz = 0
depth = 0
for instr in a.d:
    cmd, amount = instr.split(' ')
    amount = int(amount)
    if cmd == "forward":
        horz += amount
    elif cmd == "down":
        depth += amount
    elif cmd == "up":
        depth -= amount
    else:
        ValueError("Unknown command:", cmd)

total = horz * depth
a.sp(total, part=1)

# Part 2
horz = 0
depth = 0
aim = 0
for instr in a.d:
    cmd, amount = instr.split(' ')
    amount = int(amount)
    if cmd == "forward":
        horz += amount
        depth += aim * amount
    elif cmd == "down":
        aim += amount
    elif cmd == "up":
        aim -= amount
    else:
        ValueError("Unknown command:", cmd)

total = horz * depth
a.sp(total, part=2)
