with open('input.txt', 'rt') as f:
    input_data = f.readlines()
    
instructions = [ x.strip() for x in input_data ]

location = {"x": 0, "y": 0, "d": 90}

for instruction in instructions:
    action = instruction[0]
    value = int(instruction[1:])
    if action == "N":
        location["y"] += value
    elif action == "S":
        location["y"] -= value
    elif action == "E":
        location["x"] += value
    elif action == "W":
        location["x"] -= value
    elif action == "L":
        location["d"] = ( location["d"] - value ) % 360
    elif action == "R":
        location["d"] = ( location["d"] + value ) % 360
    elif action == "F":
        if location["d"] == 0:
            location["y"] += value
        elif location["d"] == 90:
            location["x"] += value
        elif location["d"] == 180:
            location["y"] -= value
        elif location["d"] == 270:
            location["x"] -= value
        else:
            raise ValueError("Non-supported direction!")

manhattan_pos = abs(location["x"]) + abs(location["y"])
print("Manhattan position:", manhattan_pos)
