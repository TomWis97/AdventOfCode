f = open('input.txt', 'rt')

current_line = ""
next_line = ""
x_pos = 0
trees = 0
line_nr = 0
for line in f.readlines():
    line_nr += 1
    current_line = next_line
    next_line = line.strip()
    if current_line == "":
        # First line
        continue
    x_pos += 3
    column = x_pos % len(next_line)
    if next_line[column] == "#":
        trees += 1
print("Trees:", trees)    
