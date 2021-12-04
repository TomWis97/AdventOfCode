def calc_trees(right, down):
    f = open('input.txt', 'rt')
    current_line = ""
    next_line = ""
    x_pos = 0
    trees = 0
    line_nr = 0
    skip_line = 0
    for line in f.readlines():
        line_nr += 1
        current_line = next_line
        next_line = line.strip()
        if skip_line > 0:
            skip_line -= 1
            continue
        else:
            skip_line = down - 1
        if current_line == "":
            # First line
            continue
        x_pos += right
        column = x_pos % len(next_line)
        if next_line[column] == "#":
            trees += 1
    return trees

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total = 0
for step in steps:
    if total == 0:
        total = calc_trees(step[0], step[1])
    else:
        total = total * calc_trees(step[0], step[1])

print("Total:", total)
print("Trees:", calc_trees(3, 1))
