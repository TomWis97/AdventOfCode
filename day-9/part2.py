with open('input.txt', 'rt') as f:
    input_data = f.readlines()

def get_valids(data, preamble_length, start):
    valid_numbers = []
    for number1 in data[start:start + preamble_length]:
        for number2 in data[start:start + preamble_length]:
            if number1 == number2:
                # Any combination, so not twice the same
                continue
            valid_numbers.append(number1 + number2)
    return valid_numbers

data = []
for line in input_data:
    data.append(int(line))

preamble_length = 25

def find_invalid(data):
    for item_position in range(len(data)):
        if item_position < preamble_length:
            continue
        line = data[item_position]
        if not int(line) in get_valids(data, preamble_length, item_position - preamble_length):
            print("Number {} is not valid!".format(line))
            return line

target = find_invalid(data)

for start_pos in range(len(data)):
    for length in range(len(data) - start_pos):
        items = data[start_pos:start_pos + length]
        if sum(items) == target:
            result = min(items) + max(items)
            print("Result:", result)
            exit()
