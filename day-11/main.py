with open('input.txt', 'rt') as f:
    input_data = f.readlines()

grid = []
for row_raw in input_data:
    row = []
    for seat in row_raw.strip():
        row.append(seat)
    grid.append(row)

# Location is a tuple (x, y). 
# Top-left is (0,0)

def check_adjacent(location, data):
    occupied_adjacent = 0
    # Row above
    if location[1] > 0:
        # We've got a row above.
        if location[0] > 0:
            # We have a row to our left
            if data[location[1]-1][location[0]-1] == "#":
                occupied_adjacent += 1
        if data[location[1]-1][location[0]] == "#":
            # We can assume that we have an item above us
            occupied_adjacent += 1
        if location[0] < len(data[location[1]]) - 1:
            # We have a row to our right
            if data[location[1]-1][location[0]+1] == "#":
                occupied_adjacent += 1
    # Current row
    if location[0] > 0:
        # We have a row to our left
        if data[location[1]][location[0]-1] == "#":
            occupied_adjacent += 1
    if location[0] < len(data[location[1]]) - 1:
        # We have a row to our right
        if data[location[1]][location[0]+1] == "#":
            occupied_adjacent += 1

    # Row below
    if location[1] < len(data)-1:
        # We've got a row below.
        if location[0] > 0:
            # We have a row to our left
            if data[location[1]+1][location[0]-1] == "#":
                occupied_adjacent += 1
        if data[location[1]+1][location[0]] == "#":
            # We can assume that we have an item above us
            occupied_adjacent += 1
        if location[0] < len(data[location[1]]) - 1:
            # We have a row to our right
            if data[location[1]+1][location[0]+1] == "#":
                occupied_adjacent += 1
    return occupied_adjacent

def run_round(data):
    new_data = [ x.copy() for x in data.copy() ]

    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "L":
                # Check if should be occupied
                if check_adjacent((x, y), data) == 0:
                    new_data[y][x] = "#"
            if data[y][x] == "#":
                # Check if should be empty
                if check_adjacent((x, y), data) > 3:
                    new_data[y][x] = "L"
    return new_data

runs = 0
while True:
    runs += 1
    old_grid = [ x.copy() for x in grid.copy() ]
    grid = run_round(grid)
    if grid == old_grid:
        break

occupied_seats = 0
for line in grid:
    for column in line:
        if column == "#":
            occupied_seats += 1

print("Occupied seats:", occupied_seats)
